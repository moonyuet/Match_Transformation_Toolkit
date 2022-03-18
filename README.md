**Match Transformation Toolkit in Blender** 

As it is only used for educational purpose only, I don't include shell scripts or batch files in this repository. I also don't include the header for the match transformation toolkit in Blender too. If you want to autoload in Blender, please refer to some of my other blender scripts(https://github.com/moonyuet/blenderTextureInput/blob/main/textureInput/TexturewithPattern.py) as references to create bl_info for the script.

**What is match transformation?**
It is basically getting all transform data(translate, rotate and scale) from object A and transfer to become the new transform attribute of object B.
This kind of data transfer is common in dcc software. Baking map and transferring UVs share similar theories with match transformation. It's essential to know in spite of its simplicity. 

**How it works programmatically in Maya?**(You can refer to [matchTransformationExplanation.py](https://github.com/moonyuet/Match_Transformation_Toolkit/blob/main/Maya/matchTransformationExplanation.py))
1. Select more than one object, and create a Python list to include them.
2. Find the last item (the parent object) from the list and get the transform data of the item.
3. Set attributes of the other items(the children objects) with the transform data got from the last item. 

**How we can replicate the similar functions in Blender?**
1. Get your selected objects and create a list
2. Get the last item of the selected object and set the variable to indicate the last item. 
3. Remove the last item of the selected object
4. set the selected objects in the list equal to the transform attirbute of the last item.
