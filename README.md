# TumorModelGenerator

## Description
A tool I developed during my time at the FDA to converts cross section breast image slices from a Digital Breast Tomosynthesis into a VDB file. The intial subsection image files were .raw files that came from the VICTRE pipeline that I ported to python. This .raw file is converted froma raw file into 201 png breast image slices through imageJ. The VDBGeneerator.py was then used to convert those 201 image slices into a 3D VDB that can be viewed through Mitsuba or Blender. There was also goals to use the this tool, as well as the VICTRE pipeline, to create skin tumor models to produce synthetic dermascope images. There are also three example VDB files in this repository. 
