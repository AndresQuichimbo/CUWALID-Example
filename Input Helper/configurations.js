const jsonConfigurations = {
    "cuwalid": {
        "run_STORM": { "default": true, "required": true, "description": "Run the STORM model" },
        "run_stoPET": { "default": true, "required": true, "description": "Run the stoPET model" },
        "run_DRYP": { "default": true, "required": true, "description": "Run the DRYP model" },
        "run_WaterCast": { "default": true, "required": true, "description": "Run the WaterCast model" },
        "sim_in_parallel": { "default": true, "required": false, "description": "Run simulations in parallel" },
    
        "forecasting_model_name": { "default": "MAM_2025_realization", "required": true, "description": "Name of the forecasting model" },
    
        "historical": {
            "model_name": { "default": "historical_model_name", "required": true, "description": "Name of the historical model" },
            "main_path": { "default": "main_path", "required": true, "description": "Path to main directory" },
            "model_path": { "default": "model_path", "required": true, "description": "Path to the model files" },
            "postpp_path": { "default": "postpp_path", "required": true, "description": "Path to post-processing files" }
        },
    
        "output_dir": { "default": "", "required": false, "description": "Directory for output files" },
    
        "Tercile_Pre_path": { 
            "default": "input/input_files/Ens_Prec_2monLead_MAM_Prob_LogitWVGEnsRegrCPT-avgRaw2025.nc", 
            "required": true, 
            "description": "Path to the precipitation tercile input file" 
        },
        "Tercile_Tem_path": { 
            "default": "input/input_files/Ens_Tref_2monLead_MAM_Raw_2025.nc", 
            "required": true, 
            "description": "Path to the temperature tercile input file" 
        },
    
        "season": { "default": ["MAM", "OND"], "required": true, "description": "Seasons included in the simulation" },
        "year": { "default": 2022, "required": true, "description": "Target year for forecasting" },
        "NSIM": { "default": 30, "required": true, "description": "Number of simulation runs" },
    
        "MODELS": {
            "DRYP": {
                "input": { "default": "input/dryp_input.json", "required": true, "description": "Path to DRYP model input file" },
                "settings": { "default": "input/dryp_settings.json", "required": true, "description": "Path to DRYP settings file" }
            },
            "STORM": {
                "input": { "default": "input/storm_input_ICPAC.json", "required": true, "description": "Path to STORM model input file" }
            },
            "stoPET": {
                "input": { "default": "input/stopet_input_ICPAC.json", "required": true, "description": "Path to stoPET model input file" }
            },
            "WaterCast": {
                "HyCast": { "default": "input/forecast_input.json", "required": true, "description": "Path to HyCast model input file" },
                "ImCast": { "default": "input/impact_forecast_input.json", "required": true, "description": "Path to ImCast model input file" }
            }
        }
    },
    "dryp": {
        "model_name": { "default": "HAD_IMERGcv_vg_sim83_2000", "required": true, "description": "Model name used for DRYP simulations" },
        "path_input": { "default": "", "required": false, "description": "Path to input files for the model" },

        "TERRAIN": {
            "path_dem": { "default": "HAD_DEM_utm_mm.asc", "required": true, "description": "Path to the Digital Elevation Model (DEM)" },
            "path_Qo": { "default": "HAD_IMERGcv_sim83_2022_avg_Q_ini.asc", "required": true, "description": "Path to the initial discharge map" },
            "path_fdl": { "default": "HAD_flowdir_land_utm.asc", "required": true, "description": "Path to the flow direction file" },
            "path_riv_decay": { "default": "HAD_decay_utm_v2.asc", "required": true, "description": "Path to river decay factor file" },
            "path_mask": { "default": "HAD_mask_utm_m.asc", "required": true, "description": "Path to basin mask file" },
            "path_riv_len": { "default": "HAD_riv_length_utm_v2.asc", "required": true, "description": "Path to river length file" },
            "path_riv_width": { "default": "HAD_width_utm_v2.asc", "required": true, "description": "Path to river width file" },
            "path_riv_elev": { "default": "HAD_riv_elev_15pc_utm_m_sm_v3.asc", "required": true, "description": "Path to river elevation file" }
        },

        "VEGETATION": {
            "path_veg_kc": { "default": null, "required": false, "description": "Path to vegetation crop coefficient file" },
            "path_veg_lulc": { "default": null, "required": false, "description": "Path to land-use/land-cover file" }
        },

        "UNSATURATED": {
            "path_uz_theta_sat": { "default": "HAD_theta_sat_utm_m.asc", "required": true, "description": "Path to soil saturated moisture content file" },
            "path_uz_theta_awc": { "default": "HAD_theta_awc_utm.asc", "required": true, "description": "Path to soil available water content file" },
            "path_uz_theta_wp": { "default": "HAD_theta_wp_utm.asc", "required": true, "description": "Path to wilting point moisture content file" },
            "path_uz_rootdepth": { "default": "HAD_rootdepth_stocker_2023_filled_factor.asc", "required": true, "description": "Path to root depth file" },
            "path_uz_lambda": { "default": "HAD_lambdas_utm_m.asc", "required": true, "description": "Path to soil lambda parameter file" },
            "path_uz_psi": { "default": "HAD_psi_utm_m.asc", "required": true, "description": "Path to soil water potential file" },
            "path_uz_ksat": { "default": "HAD_ksat_utm_zhung.asc", "required": true, "description": "Path to saturated hydraulic conductivity file" },
            "path_uz_theta": { "default": "HAD_IMERGcv_sim83_2022_avg_tht_ini.asc", "required": true, "description": "Path to initial soil moisture file" }
        },

        "RIPARIAN": {
            "path_rp_theta_sat": { "default": "HAD_theta_sat_utm_m.asc", "required": true, "description": "Path to riparian zone soil saturated moisture content" },
            "path_rp_theta_awc": { "default": "HAD_theta_awc_utm.asc", "required": true, "description": "Path to riparian zone available water content" },
            "path_rp_theta_wp": { "default": "HAD_theta_wp_utm.asc", "required": true, "description": "Path to riparian zone wilting point moisture content" },
            "path_rp_rootdepth": { "default": "HAD_rootdepth_utm_m.asc", "required": true, "description": "Path to riparian zone root depth" },
            "path_rp_lambda": { "default": "HAD_lambdas_utm_m.asc", "required": true, "description": "Path to riparian zone soil lambda parameter" },
            "path_rp_psi": { "default": "HAD_psi_utm_m.asc", "required": true, "description": "Path to riparian zone soil water potential" },
            "path_rp_ksat": { "default": "HAD_ksat_utm_m.asc", "required": true, "description": "Path to riparian zone saturated hydraulic conductivity" },
            "path_rp_theta": { "default": "HAD_IMERGcv_sim83_2022_avg_tht_rp_ini.asc", "required": true, "description": "Path to riparian zone initial soil moisture" }
        },

        "SATURATED": {
            "path_sz_ksat": { "default": "HAD_ksat_D2E_ksat_sim_85_utm.asc", "required": true, "description": "Path to saturated zone hydraulic conductivity" },
            "path_sz_sy": { "default": "HAD_D2E_sy_ghlymps_utm_mmm.asc", "required": true, "description": "Path to saturated zone specific yield" },
            "path_sz_wte": { "default": "HAD_IMERGcu_sim83_2022_avg_wte_ini.asc", "required": true, "description": "Path to initial water table elevation" },
            "path_sz_bc_head": { "default": "HAD_CHBm_utm.asc", "required": true, "description": "Path to boundary condition head" },
            "path_sz_bottom": { "default": "HAD_botb.asc", "required": true, "description": "Path to saturated zone bottom boundary" },
            "path_sz_depth": { "default": "HAD_BDdepth_utm_m_sm_v2.asc", "required": true, "description": "Path to saturated zone depth" },
            "path_sz_type": { "default": "HAD_globathymetry_utm.asc", "required": true, "description": "Path to saturated zone type classification" }
        },

        "METEO": {
            "path_pre": { "default": "input/input_files/Ens_Prec_2monLead_MAM_Prob_LogitWVGEnsRegrCPT-avgRaw2025.nc", "required": true, "description": "Path to precipitation input file" },
            "path_pet": { "default": "input/input_files/Ens_Tref_2monLead_MAM_Raw_2025.nc", "required": true, "description": "Path to potential evapotranspiration input file" },
            "path_lai": { "default": null, "required": false, "description": "Path to leaf area index file" },
            "path_savi": { "default": null, "required": false, "description": "Path to soil-adjusted vegetation index file" },
            "path_kc": { "default": null, "required": false, "description": "Path to crop coefficient file" }
        },

        "WATER_BODIES": {
            "path_lake_depth": { "default": "HAD_globathymetry_utm.asc", "required": true, "description": "Path to lake depth file" },
            "path_pnd_hmax": { "default": "HAD_ali2024_ponds_max_depth_utm_no_lakes.asc", "required": true, "description": "Path to maximum pond depth file" },
            "path_pnd_Amax": { "default": "HAD_ali2024_ponds_max_area_utm_no_lakes.asc", "required": true, "description": "Path to maximum pond area file" }
        },

        "INTERCEPTION": {
            "path_veg_rp_extinction_depth": { "default": "HAD_rootdepth_stocker_2023_filled.asc", "required": true, "description": "Path to extinction depth for riparian vegetation" }
        },

        "OUTPUT": {
            "path_out_sz": { "default": "HAD_dryp_station_utm.csv", "required": true, "description": "Output path for saturated zone data" },
            "path_out_uz": { "default": "HAD_dryp_station_utm.csv", "required": true, "description": "Output path for unsaturated zone data" },
            "path_out_oz": { "default": "HAD_dryp_station_utm.csv", "required": true, "description": "Output path for other zone data" },
            "path_output": { "default": "/home/cuwalid/training/forecast/regional/outputs", "required": true, "description": "Main output directory" },
            "path_setting": { "default": "input/dryp_settings.json", "required": true, "description": "Path to settings file" },
            "path_projection": { "default": "HAD_projection.dwapm", "required": true, "description": "Path to projection file" }
        }
    },
    "dryp_settings": {
        "SIMULATION_PERIOD": {
            "start_date": {
                "default": "2024 3 1",
                "required": true,
                "description": "Day of the year that the model should start from"
            },
            "end_date": {
                "default": "2024 5 30",
                "required": true,
                "description": "Day of the year that the model should end at"
            }
        },
        "PROJECTION": {
            "default": "+proj=laea +lat_0=5 +lon_0=20 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs",
            "required": true,
            "description": "Projection system used for spatial calculations"
        },
        "TIMESTEP_SETTINGS": {
            "dt_of": {
                "default": 60,
                "required": true,
                "description": "Timestep for overland flow calculations (in minutes)"
            },
            "dt_uz": {
                "default": 60,
                "required": true,
                "description": "Timestep for unsaturated zone calculations (in minutes)"
            },
            "dt_gw": {
                "default": 60,
                "required": true,
                "description": "Timestep for groundwater calculations (in minutes)"
            }
        },
        "READING": {
            "data_reading": {
                "pre": {
                    "default": 5,
                    "required": true,
                    "description": "Precipitation data reading interval"
                },
                "pet": {
                    "default": 1,
                    "required": true,
                    "description": "Potential evapotranspiration data reading interval"
                },
                "kc": {
                    "default": 3,
                    "required": true,
                    "description": "Crop coefficient data reading interval"
                },
                "savi": {
                    "default": 3,
                    "required": true,
                    "description": "Soil-adjusted vegetation index data reading interval"
                },
                "lai": {
                    "default": 3,
                    "required": true,
                    "description": "Leaf area index data reading interval"
                }
            },
            "data_step": {
                "pre": {
                    "default": 30,
                    "required": true,
                    "description": "Precipitation data timestep (in minutes)"
                },
                "pet": {
                    "default": 60,
                    "required": true,
                    "description": "Potential evapotranspiration data timestep (in minutes)"
                },
                "kc": {
                    "default": 1440,
                    "required": true,
                    "description": "Crop coefficient data timestep (in minutes)"
                },
                "savi": {
                    "default": 1440,
                    "required": true,
                    "description": "Soil-adjusted vegetation index data timestep (in minutes)"
                },
                "lai": {
                    "default": 1440,
                    "required": true,
                    "description": "Leaf area index data timestep (in minutes)"
                }
            },
            "data_reproject": {
                "pre": {
                    "default": false,
                    "required": true,
                    "description": "Whether to reproject precipitation data"
                },
                "pet": {
                    "default": true,
                    "required": true,
                    "description": "Whether to reproject potential evapotranspiration data"
                },
                "kc": {
                    "default": false,
                    "required": true,
                    "description": "Whether to reproject crop coefficient data"
                },
                "savi": {
                    "default": false,
                    "required": true,
                    "description": "Whether to reproject soil-adjusted vegetation index data"
                },
                "lai": {
                    "default": false,
                    "required": true,
                    "description": "Whether to reproject leaf area index data"
                }
            },
            "data_interp": {
                "pre": {
                    "default": true,
                    "required": true,
                    "description": "Whether to interpolate precipitation data"
                },
                "pet": {
                    "default": true,
                    "required": true,
                    "description": "Whether to interpolate potential evapotranspiration data"
                },
                "kc": {
                    "default": false,
                    "required": true,
                    "description": "Whether to interpolate crop coefficient data"
                },
                "savi": {
                    "default": false,
                    "required": true,
                    "description": "Whether to interpolate soil-adjusted vegetation index data"
                },
                "lai": {
                    "default": false,
                    "required": true,
                    "description": "Whether to interpolate leaf area index data"
                }
            },
            "data_projection": {
                "pre": {
                    "default": "EPSG:42106",
                    "required": true,
                    "description": "Projection used for precipitation data"
                },
                "pet": {
                    "default": "EPSG:4326",
                    "required": true,
                    "description": "Projection used for potential evapotranspiration data"
                },
                "kc": {
                    "default": "EPSG:4326",
                    "required": true,
                    "description": "Projection used for crop coefficient data"
                },
                "savi": {
                    "default": "EPSG:4326",
                    "required": true,
                    "description": "Projection used for soil-adjusted vegetation index data"
                },
                "lai": {
                    "default": "EPSG:4326",
                    "required": true,
                    "description": "Projection used for leaf area index data"
                }
            }
        },
        "COMPONENTS": {
            "method_inf": {
                "default": 1,
                "required": true,
                "description": "Method used for infiltration calculation"
            },
            "run_gw": {
                "default": true,
                "required": true,
                "description": "Whether to include groundwater simulation"
            },
            "method_gw": {
                "default": 0,
                "required": true,
                "description": "Method used for groundwater simulation"
            }
        },
        "OUTPUT": {
            "output_csv": {
                "default": true,
                "required": true,
                "description": "Whether to output data in CSV format"
            },
            "output_grid": {
                "default": true,
                "required": true,
                "description": "Whether to output data in grid format"
            },
            "output_dt": {
                "default": "1M",
                "required": true,
                "description": "Time interval for output data (e.g., daily, monthly, etc.)"
            }
        },
        "GLOBAL_FACTORS": {
            "uz_kdt": {
                "default": "1.0",
                "required": true,
                "description": "Unsaturated zone decay time factor"
            },
            "uz_kdroot": {
                "default": "1.5",
                "required": true,
                "description": "Root zone decay factor"
            },
            "uz_kawc": {
                "default": "1.0",
                "required": true,
                "description": "Available water capacity factor in the unsaturated zone"
            },
            "uz_kkast": {
                "default": "0.7",
                "required": true,
                "description": "Karstification coefficient for the unsaturated zone"
            },
            "uz_ksigma": {
                "default": "1.0",
                "required": true,
                "description": "Sigma coefficient for the unsaturated zone"
            },
            "riv_kksat": {
                "default": "0.87",
                "required": true,
                "description": "Saturated hydraulic conductivity factor for river channels"
            },
            "riv_kdecay": {
                "default": "20.3",
                "required": true,
                "description": "Decay factor for river infiltration"
            },
            "riv_kwidth": {
                "default": "1",
                "required": true,
                "description": "Width factor for river channels"
            },
            "sz_kksat": {
                "default": "1.10",
                "required": true,
                "description": "Saturated hydraulic conductivity factor for the saturated zone"
            },
            "sz_ksy": {
                "default": "0.82",
                "required": true,
                "description": "Specific yield coefficient for the saturated zone"
            }
        }
    },
    "storm": {
        "NUMSIMS": {
            "default": 30,
            "required": true,
            "description": "Number of storm simulations to run"
        },
        "NUMSIMYRS": {
            "default": 1,
            "required": true,
            "description": "Number of simulation years"
        },
        "SEASON_TAG": {
            "default": "MAM",
            "required": true,
            "description": "Seasonal tag indicating the time period of simulation (e.g., MAM, OND)"
        },
        "SEED_YEAR": {
            "default": 2025,
            "required": true,
            "description": "Base year for stochastic storm simulations"
        },
        "PDF_FILE": {
            "default": "./model_input/ProbabilityDensityFunctions.csv",
            "required": true,
            "description": "Path to the probability density function file"
        },
        "SHP_FILE": {
            "default": "./model_input/HAD_basin.shp",
            "required": true,
            "description": "Path to the shapefile containing basin boundaries"
        },
        "DEM_FILE": {
            "default": "./model_input/HAD_wgs84.tif",
            "required": true,
            "description": "Path to the Digital Elevation Model (DEM) file"
        },
        "ZON_FILE": {
            "default": "./model_input/regions.shp",
            "required": true,
            "description": "Path to the shapefile defining simulation regions"
        },
        "TER_FILE": {
            "default": "./model_input/tercilesICPAC_OND_2024.shp",
            "required": true,
            "description": "Path to the shapefile containing tercile-based seasonal forecasts"
        },
        "OUT_PATH": {
            "default": "./storm_output",
            "required": true,
            "description": "Directory where storm model outputs will be saved"
        },
        "RAIN_MAP": {
            "default": "./model_input/rainfall_OND.nc",
            "required": true,
            "description": "Path to the NetCDF file containing rainfall data for the given season"
        }
    },
    "stopet": {
        "execution_type": {
            "default": "hpc",
            "required": true,
            "description": "Type of execution environment (recommended to use hpc)"
        },
        "outputpath": {
            "default": "",
            "required": true,
            "description": "Path where output files will be stored"
        },
        "runtype": {
            "default": "regional",
            "required": true,
            "description": "Type of simulation run (e.g., regional, local)"
        },
        "startyear": {
            "default": 2025,
            "required": true,
            "description": "Starting year of the simulation"
        },
        "endyear": {
            "default": 2025,
            "required": true,
            "description": "Ending year of the simulation"
        },
        "seasonswitch": {
            "default": 1,
            "required": true,
            "description": "Flag to indicate seasonal mode (1 for active, 0 for inactive)"
        },
        "startdate": {
            "default": 274,
            "required": true,
            "description": "Julian day representing the start date of the simulation"
        },
        "enddate": {
            "default": 365,
            "required": true,
            "description": "Julian day representing the end date of the simulation"
        },
        "seasonName": {
            "default": "MAM",
            "required": true,
            "description": "Name of the season for the simulation"
        },
        "latval": {
            "default": 1.0,
            "required": true,
            "description": "Latitude value for a specific location"
        },
        "lonval": {
            "default": 35.0,
            "required": true,
            "description": "Longitude value for a specific location"
        },
        "latval_min": {
            "default": -7.0,
            "required": true,
            "description": "Minimum latitude value for the region"
        },
        "latval_max": {
            "default": 16.0,
            "required": true,
            "description": "Maximum latitude value for the region"
        },
        "lonval_min": {
            "default": 31.0,
            "required": true,
            "description": "Minimum longitude value for the region"
        },
        "lonval_max": {
            "default": 52.1,
            "required": true,
            "description": "Maximum longitude value for the region"
        },
        "number_ensm": {
            "default": 3,
            "required": true,
            "description": "Number of ensemble members in the simulation"
        },
        "tempAdj": {
            "default": 2,
            "required": true,
            "description": "Temperature adjustment factor"
        },
        "deltat": {
            "default": 0.0,
            "required": true,
            "description": "Time step adjustment parameter"
        },
        "locname": {
            "default": "HAD",
            "required": true,
            "description": "Location name associated with the simulation"
        },
        "udpi_pet": {
            "default": 5,
            "required": true,
            "description": "PET (Potential Evapotranspiration) update interval in days"
        },
        "slice_only": {
            "default": 0,
            "required": true,
            "description": "Flag to indicate if only a slice of data is used (1 for true, 0 for false)"
        },
        "tercile_forecast_file": {
            "default": "input/input_files/Ens_Tref_2monLead_MAM_Raw_2025.nc",
            "required": true,
            "description": "Path to the tercile forecast NetCDF file"
        }
    },
    "forecast": {
        "run_historical": {
            "default": false,
            "required": true,
            "description": "Flag to enable historical simulation run"
        },
        "run_forecast": {
            "default": false,
            "required": true,
            "description": "Flag to enable forecast simulation run"
        },
        "run_plotting": {
            "default": false,
            "required": true,
            "description": "Flag to enable plotting of results"
        },
        "multi_files": {
            "default": true,
            "required": true,
            "description": "Flag to indicate if multiple input files are used"
        },
        "historical": {
            "model_name": {
                "default": "HAD_IMERGcv_input_sim85_test",
                "required": true,
                "description": "Name of the historical model"
            },
            "model_path": {
                "default": "",
                "required": true,
                "description": "Path to the historical model files"
            },
            "postpp_path": {
                "default": "/home/cuwalid/training/historical/regional/postpp/",
                "required": true,
                "description": "Path to the post-processing directory for historical data"
            }
        },
        "forecasting": {
            "model_name": {
                "default": "MAM_2025_realization",
                "required": true,
                "description": "Name of the forecasting model"
            },
            "model_path": {
                "default": "/home/cuwalid/training/forecast/regional/outputs/",
                "required": true,
                "description": "Path to the forecasting model output files"
            },
            "postpp_path": {
                "default": "/home/cuwalid/training/forecast/regional/postpp/",
                "required": true,
                "description": "Path to the post-processing directory for forecast data"
            }
        },
        "threshold_path": {
            "default": "/home/cuwalid/training/historical/regional/postpp/netcdf/",
            "required": true,
            "description": "Path to the threshold NetCDF files"
        },
        "season": {
            "default": ["MAM", "OND"],
            "required": true,
            "description": "List of seasons included in the simulation"
        },
        "start_year": {
            "default": 2025,
            "required": true,
            "description": "Start year of the forecast simulation"
        },
        "end_year": {
            "default": 2025,
            "required": true,
            "description": "End year of the forecast simulation"
        },
        "year": {
            "default": 2025,
            "required": true,
            "description": "Year for the forecast simulation"
        },
        "variables": {
            "pre": {
                "default": true,
                "required": true,
                "description": "Precipitation variable"
            },
            "pet": {
                "default": true,
                "required": true,
                "description": "Potential Evapotranspiration variable"
            },
            "aet": {
                "default": true,
                "required": true,
                "description": "Actual Evapotranspiration variable"
            },
            "tht": {
                "default": true,
                "required": true,
                "description": "Soil moisture variable"
            },
            "egw": {
                "default": true,
                "required": true,
                "description": "Evaporation from groundwater variable"
            },
            "inf": {
                "default": false,
                "required": true,
                "description": "Infiltration variable"
            },
            "run": {
                "default": false,
                "required": true,
                "description": "Surface runoff variable"
            },
            "rch": {
                "default": true,
                "required": true,
                "description": "Recharge variable"
            },
            "fch": {
                "default": true,
                "required": true,
                "description": "Flow change variable"
            },
            "gdh": {
                "default": true,
                "required": true,
                "description": "Groundwater depth variable"
            },
            "dis": {
                "default": true,
                "required": true,
                "description": "Discharge variable"
            },
            "tls": {
                "default": false,
                "required": true,
                "description": "Total land storage variable"
            },
            "wte": {
                "default": true,
                "required": true,
                "description": "Water table elevation variable"
            },
            "twsc": {
                "default": true,
                "required": true,
                "description": "Terrestrial Water Storage Change variable"
            },
            "wrsi": {
                "default": false,
                "required": true,
                "description": "Water Requirement Satisfaction Index variable"
            },
            "flood": {
                "default": true,
                "required": true,
                "description": "Flood extent variable"
            }
        }
    },
    "impact_forecast": {
        "create_dataset": {
            "default": false,
            "required": true,
            "description": "Flag to enable dataset creation"
        },
        "create_table": {
            "default": false,
            "required": true,
            "description": "Flag to enable table creation"
        },
        "create_map": {
            "default": true,
            "required": true,
            "description": "Flag to enable map creation"
        },
        "plot_scales": {
            "default": ["County", "Country", "Zoom", "Ward"],
            "required": true,
            "description": "Scale at which the data should be plotted"
        },
        "country": {
            "default": ["somalia", "ethiopia", "kenya"],
            "required": true,
            "description": "List of countries included in the forecast"
        },
        "place_names": {
            "default": [],
            "required": true,
            "description": "List of specific place names to include (if applicable)",
            "type": "custom" // Setting it as custom means the user can enter their own things to be added to the list
        },
        "seasons": {
            "default": ["OND", "MAM"],
            "required": true,
            "description": "List of seasons included in the impact forecast"
        },
        "water_status": {
            "default": ["Groundwater", "Flood", "Surface", "Soil", "Crop"],
            "required": true,
            "description": "Types of water-related statuses included in the forecast"
        },
        "year": {
            "default": 2025,
            "required": true,
            "description": "Year for the impact forecast"
        },
        "language": {
            "default": "English",
            "required": true,
            "description": "Language in which the forecast results are presented"
        },
        "output_dir": {
            "default": "/home/cuwalid/training/forecast/regional/postpp/",
            "required": true,
            "description": "Directory where forecast output files will be stored"
        },
        "netcdf_path": {
            "default": "MAM_2022_realization_twsc_MAM_2022_probabilistic_tercile_forecast.nc",
            "required": true,
            "description": "Path to the NetCDF file used for the forecast"
        },
        "model_name": {
            "default": "HAD_IMERGba_sim0",
            "required": true,
            "description": "Name of the forecasting model used"
        },
        "parameter_dataset_list": {
            "default": "/home/cuwalid/training/forecasting_model_files/parameters_dataset_list_ICPAC.json",
            "required": true,
            "description": "Path to the parameter dataset list file"
        }
    }
};