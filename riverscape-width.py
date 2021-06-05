

# ---- Set Up ----

# check projection - needs to be in a local projection with meters as the measurement unit

# user parameters
max_vb_width = 300
transect_distance = 10
segment_length = 100

# trash path
trash_path = '/Users/nick/Desktop/riverscape-network/trash-output/segmented.gpkg'



# Choose an output working directory


# Choose network centerline layer


# Choose surface extent polygon layer




# --- Segment the network ---

# first just get a center line to work with
center_line = iface.layerTreeView().selectedLayers()[0]


# TODO specify output file path


# segment the line
processing.run("native:splitlinesbylength",
    {'INPUT':'/Users/nick/Desktop/riverscape-network/start/center-projected.gpkg|layername=center-projected',
    'LENGTH':segment_length,
    'OUTPUT':'memory:'})

# --- Add valley cross sections ---

# add points at intervals
processing.run("native:pointsalonglines",
    {'INPUT':'/Users/nick/Desktop/riverscape-network/start/center-projected.gpkg|layername=center-projected',
    'DISTANCE':transect_distance,
    'START_OFFSET':0,
    'END_OFFSET':0,
    'OUTPUT':'TEMPORARY_OUTPUT'})




