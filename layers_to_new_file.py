from gimpfu import *

#copy visible layers to a new file, if mask exist, copy the mask too
def to_new_image(image, drawable):    
    layers = [] #list of active layers

    try:
        #get every active layer
        listAllVisible(image, layers)

        #create new image and insert blank layer
        newImage = gimp.Image(image.width, image.height, RGB)
        newLayer = gimp.Layer(newImage, "temp", newImage.width, newImage.height, RGBA_IMAGE, 100, NORMAL_MODE)
        newImage.add_layer(newLayer, 0)

        for layer in layers:
            #select the layer, copy, and paste it into newImage as new floating layer
            pdb.gimp_image_select_item(image, 0, layer)
            pdb.gimp_edit_copy(layer)
            floatLayer = pdb.gimp_edit_paste(newLayer, True)
            
            #take floating layer and turn to new layer
            pdb.gimp_floating_sel_to_layer(floatLayer)

            floatLayer.name = layer.name

            #if a mask exists
            if layer.mask != None:
                mask = floatLayer.create_mask(ADD_MASK_WHITE)
                floatLayer.add_mask(mask)

                #get channel from original layer
                maskChannel = layer.mask

                pdb.gimp_channel_combine_masks(mask, maskChannel, 2, 0, 0)
    
        gimp.Display(newImage)
        gimp.displays_flush()
        pdb.gimp_selection_none(image)

    except Exception as e:
        pdb.gimp_message(e.args[0])

    return


def listAllVisible(parent, outputList):
    for layer in parent.layers:
        if pdb.gimp_layer_get_visible(layer):
            outputList.append(layer)
            if pdb.gimp_item_is_group(layer):
                listAllVisible(layer, outputList)

register(
    "Layers_To_New_File",
    "Takes visible layers and copys them to new file",
    "Copy layers to new file",
    "Sophia Lilmohan",
    "Sophia Lilmohan",
    "2023",
    "<Image>/Functionality/Layers_To_New_File",
    "*",
    [],
    [],
    to_new_image)


main()