# Install guide
This is an installation guide for the Linux PC this was tested on. For other computers/servers, the wheel files may need to be built for that architecture. See the [ecoshard](https://github.com/matthewharris02/ecoshard-fork) and [inspring](https://github.com/matthewharris02/inspring-fork) forked repositories for guidance.

- In a virtual environment, do the following:
  - Install gdal version 3.10.2 (for this computer, this was the most recent available version): `python -m pip install gdal==3.10.2`
  - Install ecoshard from wheel: `python -m pip install [ecoshard-wheel].whl`
  - Install inspring from wheel: `python -m pip install [inspring-wheel].whl`
  - Install pandas (missing in inspring requirements and couldn't get it to work): `python -m pip install pandas`

# Usage guide
Usage follows the README and InVEST guide. Make sure that the python files are exceuted in the virtual environment that the above was installed in.