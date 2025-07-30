"""
File Name: height_above_ground.py
Author: Ian Horn
Data: 2025-07-30
Description: This script uses a PDAL Pipeline to filter first returns and
             calculate a height above ground value. This resulting file can
             then be processed to create a surface model.
Environment: mamba create --name <env_name>
             conda init
             mamba activate <env_name>
             mamba install -c conda-forge python-pdal
"""

import os
import json
import pdal
from tqdm import tqdm

copc_laz_file = 'https://kyfromabove.s3.us-west-2.amazonaws.com/elevation/PointCloud/Phase2/N110E348_LAS_Phase2.copc.laz'
output_dir = 'downloads/hag'  # output location
f_basename = os.path.basename(copc_laz_file)
hag_filename = f"{output_dir}/{f_basename.replace('.copc.laz', '_hag.copc.laz')}"
dsm_filename = f"{output_dir}/{f_basename.replace('.copc.laz', '_hag.tif')}"

# create directory if does not exists
if not os.path.exists(output_dir): 
    os.makedirs(output_dir)

json_pipe = [
    {
        "type":"readers.copc",
        "filename":copc_laz_file        
    },
    {
        "type":"filters.expression",
        "expression":"ReturnNumber == 1 || NumberOfReturns == 1"  # grabs all first returns
    },
    {
        "type":"writers.copc",
        "filename":hag_filename
    },
    {
        "type":"filters.hag_delaunay",
        "allow_extrapolation":True
    },
    {
        "type":"filters.ferry",  # carries the values to the new file
        "dimensions":"HeightAboveGround=>Z"
    },
    {
        "type":"writers.gdal",
        "filename":dsm_filename,
        "resolution":2,
        "output_type":"max",
        "nodata":-999999,
        "gdalopts":[
            "COMPRESS=LZW",
            "TILED=YES",
            "BLOCKXSIZE=256",
            "BLOCKYSIZE=256"
        ]
    }
]

pipeline = pdal.Pipeline(json.dumps(json_pipe))
count = pipeline.execute()
arrays = pipeline.arrays
metadata = pipeline.metadata
log = pipeline.log
print(f"Pipeline executed with {count} points processed.")  