Nutrient and Sediment Delivery Computational Pipeline
=====================================================

This project executes variants of the InVEST NDR and SDR models that allow for continuous biophysical data layers rather than the reliance of a landcover-to-lookup table based map. It is also a data pipeline that breaks large landscape analyses into smaller landscape components that can be processed in parallel. In short, use this project if you:

1) want to run the InVEST NDR or SDR models on very large datasets (50k x 50k raster sizes or more), and/or,
2) have direct Earth Observation based data that you want to use instead of a landcover map (ex: a C factor raster built from an ML model of NDVI).

Configure the model run by defining necessary variables in an .ini file, examples located in ``pipeline_config_files``. For example, the following configuration file defines a run of SDR on a single watershed where ``FERTILIZER``, ``EROSIVITY``, ``ERODIBILITY``, and ``RUNOFF_PROXY`` are rasters defined on a remote server, ``USLE_C`` and ``USLE_P`` are local continuous rasters. Any data not listed are defaulted in ``global_config.ini`` but can be overridden.

    [wwf_IDN_baseline_debug_c_p_factor_rasters]
    TARGET_PIXEL_SIZE_M = 30
    GLOBAL_PIXEL_SIZE_DEG = 0.00027777777777778
    L_CAP = 122
    K_PARAM = 2
    SDR_MAX = 0.8
    IC_0_PARAM = 0.5
    FERTILIZER = https://storage.googleapis.com/ecoshard-root/key_datasets/fertilizers/nci_current_n_app_extens_background_md5_42b028.tif
    EROSIVITY = https://storage.googleapis.com/ecoshard-root/key_datasets/GlobalR_NoPol_compressed_md5_49734c4b1c9c94e49fffd0c39de9bf0c.tif
    ERODIBILITY = https://storage.googleapis.com/ecoshard-root/key_datasets/Kfac_SoilGrid1km_GloSEM_v1.1_md5_e1c74b67ad7fdaf6f69f1f722a5c7dfb.tif
    RUNOFF_PROXY = https://storage.googleapis.com/ecoshard-root/key_datasets/worldclim_2015_md5_16356b3770460a390de7e761a27dbfa1.tif
    USLE_C = D:/repositories/spring/ndr_sdr_global/test_data/usle_c_wwf_IDN_baseline_debug.tif
    USLE_P = D:/repositories/spring/ndr_sdr_global/test_data/usle_p_wwf_IDN_baseline_debug.tif
    RUN_NDR=False
    RUN_SDR=True
    KEEP_INTERMEDIATE_FILES=True
    WATERSHED_SUBSET = {'as_bas_15s_beta': [576264]}

To run the model execute the main script and pass any number of ``.ini`` files at the command line, for example: ``python run_ndr_sdr_pipeline.py wwf_IDN_baseline_debug_c_p_factor_rasters.ini`` During execution a log file is streamed to ``sdrndrlog.txt`` which can be watched with a ``tail -f sdrndrlog.txt`` command.

Final results will be located in a directory called ``workspace_{basename of ini file}`` so the example above will be located at ``workspace_wwf_IDN_baseline_debug_c_p_factor_rasters``.

The InVEST user's guide for these models is comparable, except for the option to provide custom continuous raster data in leiu of a landcover/lookup table combination:

* SDR: <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/en/sdr.html>
* NDR: <https://storage.googleapis.com/releases.naturalcapitalproject.org/invest-userguide/latest/en/ndr.html>
