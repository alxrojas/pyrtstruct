# pyrtstruct

__author__ = 'Alejandro Rojas-Lopez, Sofia , Nicola , Martin, Jeronimo '
__copyright__ = 'Copyright 2022'
__credits__ = ['Alejandro Rojas-Lopez', 'Sofia Peron', 'Nicola 'Maddalozzo',
                'Martin ', 'Jeronimo ']
__version__ = "1.0"
__maintainer__ = "Alejandro Rojas-Lopez"
__email__ = "alexrojas@ciencias.unam.mx"
__status__ = "On construction"

Pyrtstruct is a package for processing DICOM radiotherapy structures. It allows to extract the information from the structures in a simple “.xlsx” format. Also allows modify structures (expand, contract, rotate, translate) without using CT or MRI images and create new DICOM files with this information, which are compatible with the commercial systems of treatment planning.

The information is reported in an user-friendly form for post-statistical processing.

The code allows to handle the structure DICOM file for any contour of radiotherapy treatment plan.

The code was tested for DICOM files obtained by the treatment planning system (TPS) Brainlab Elements and Eclipse. For details contact the authors.

The code works with the structure (RS) and plan (RP) DICOM files. RS for extracting the information for each organ or lesion and RP for obtaining the information of the center of mass and the isocenter of the plan.

We recommend that RS and RP are in different directories with no other files. Example:
 ./DirectoryStructure/RS.dcm
 ./DirectoryPlan/RP.dcm

In all cases, it is responsibility of the physician and the physicist of the clinical institution to verify on their TPS the correct and final delimitation of the new margins before treatment. The authors assume no responsibility for the missuse or missunderstanding of the results of this code.
