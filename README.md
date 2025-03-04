# kyfromabove-on-aws-examples
This repo contains examples of how to access KyFromAbove hosted on AWS's open data registry.  You can find the sample notebooks in the [example folder](examples).

## Resources

KyFromAbove [Open Data Registry](https://registry.opendata.aws/kyfromabove/) on AWS<br>
KyFomAbove AWS [Open Data Docs](https://github.com/awslabs/open-data-docs/tree/main/docs/kyfromabove)<br>
KyFromAbove [AWS Data Explorer](https://kyfromabove.s3.us-west-2.amazonaws.com/index.html)<br>
[AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) - No AWS Account Required (_Optional - but may be necessary because of the boto3 python module_)<br>
<br>
See [KyFromAbove Tile Index Geopackage Links](#kyfromabove-geopackage-links) below.

___
## Set up your environment

1. Clone this repo:
```bash
git clone https://github.com/ianhorn/kyfromabove-on-aws-examples.git
cd kyfromabove-on-aws-examples
```

Create a python environment and activate it. Make sure to use the correct commands for mac/linux or windows.

On Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
On Windows
```cmd
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
___
# Tutorials

1. Bulk download a large Area of Interest using [Phase2 DEM](#dem) for Daniel Boone National Forest [python notebook](examples/clip_tiles_to_boundary.ipynb).
2. Bulk download county images [python notebook](examples/bulk_download_county.ipynb) using [orthoimagery](#orthoimagery) geopackage and [kygisserver](https://kygisserver.ky.gov/arcgis) vector services.

___
### KyFromAbove Geopackage Links

Copy these links to use directly in the sample notebooks\*.

\* _These links are also available via the [constants.py](examples/constants.py).  I set these up to be used in the tutorials._

#### DEM


```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/DEM/TileGrids/kyfromabove_phase1_5k_dem_grid.gpkg
```
```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/DEM/TileGrids/kyfromabove_phase2_5k_dem_grid.gpkg
```

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/DEM/TileGrids/kyfromabove_phase3_5k_dem_grid.gpkg
```

#### Point Cloud

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/PointCloud/TileGrids/kyfromabove_phase1_pointcloud_5k_grid.gpkg
```

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/PointCloud/TileGrids/kyfromabove_phase2_pointcloud_5k_grid.gpkg
```

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/elevation/PointCloud/TileGrids/kyfromabove_phase3_pointcloud_5k_grid.gpkg
```

#### Orthoimagery

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/imagery/orthos/tile-grids/kyfromabove_phase1_aerial_5k_grid.gpkg
```

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/imagery/orthos/tile-grids/kyfromabove_phase2_aerial_5k_grid.gpkg
```

```bash
https://kyfromabove.s3-us-west-2.amazonaws.com/imagery/orthos/tile-grids/kyfromabove_phase3_aerial_5k_grid.gpkg
```