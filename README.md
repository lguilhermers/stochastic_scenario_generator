# scenario-generator

This City Energy Analyst plugin is used to automate a number of parallelized simulations of the same scenario **for a single building**, based on variable input stochastic distributions. An output file is produced, which saves main inputs and outputs from each iteration.

Each input parameter defined in the [0,1] domain is defined by a Beta distribution. Input parameters that are outside this domain are adjusted in location and scale by a Four parameters Beta distribution. Each distribution is restrained to minimum and maximum boundaries 

defined in CEA, as well as to theoretical boundaries considered suitable for this case study. The code is suitable to run muiltiple scenarios in paralel. For that, one copy of the scenario will be created for each CPU instance. 

This plugin aims to assist the process of data generation and collection and may used in a wide range of topics, including Monte Carlo simulations, surrogate modeling, and sensitivity analysis.


As example:

- An input, the user chooses a scenario (defined by the config file) to run 1500 iterations using 3 CPUs.

- The scenario is copied 3 times (number of CPUs), following the structure "scenarionameX", where X is the ID for each batch. In this case, "scenario0", "scenario1" and "scenario2" would be created.

- Each scenario runs radiation and demand for a different realization of the stochastic distributions for every iteration. In this example, "scenario0" would run iterations 1-500, while "scenario1" is running 501-1000 and "scenario2" is running 1001-1500.

- From every iteration, the inputs and main outputs are saved in "outputs\data\demand\data_generation.csv"

The following input parameters are considered:

zone_floors_ag,	zone_floor_to_floor_height,	surrounding_floors_ag, surroundings_floor_to_floor_height,	Hs_ag,	Es,	Ns,	void_deck,	wwr,	Cm_Af,	n50,	U_win,	G_win,	e_win,	F_F,	U_roof,	a_roof,	e_roof,	r_roof,	U_wall,	a_wall,	e_wall,	r_wall,	rf_sh,	Occ_m2p,	Qs_Wp,	X_ghp,	Ea_Wm2,	El_Wm2,	Vww_ldp,	Tcs_set_C,	Ve_lsp,	dT_Qcs,	ECONOMIZER,	HEAT_REC,	convection_cs,	dTcs_C,	efficiency_cooling

The following outputs are considered:

Annual_energy_demand_MWhyr,	GFA_m2,	EUI_kWhyr_m2,	EEI_kWhyr_m2(used in the Singapore context),	weekly_occupancy_h,	weekly_appliances_h,	weekly_lighting_h,	weekly_water_h,	weekly_cooling_h



## Installation
To install, clone this repo to a desired path (you would need to have `git` installed to run this command. Alternatively you can also run this command in the CEA console, which comes with `git` pre-installed):

```git clone https://github.com/architecture-building-systems/cea-plugin-template.git DESIRED_PATH```

Open CEA console and enter the following command to install the plugin to CEA:

```pip install -e PATH_OF_PLUGIN_FOLDER```

(NOTE: PATH_OF_PLUGIN_FOLDER would be the DESIRED_PATH + 'cea-template-plugin')


In the CEA console, enter the following command to enable the plugin in CEA:

```cea-config write --general:plugins scenario_generator.ScenarioPlugin```

NOTE: If you are installing multiple plugins, add them as a comma separated list in the `cea-config write --general:plugins ...` command.
