import adsk.core, adsk.fusion, traceback

BIN_XY_TOLERANCE = 0.025
BIN_CORNER_FILLET_RADIUS = 0.4 - BIN_XY_TOLERANCE

BIN_BASE_TOP_SECTION_HEIGH = 0.215
BIN_BASE_MID_SECTION_HEIGH = 0.18
BIN_BASE_BOTTOM_SECTION_HEIGH = 0.08
BIN_BASE_HEIGHT = BIN_BASE_TOP_SECTION_HEIGH + BIN_BASE_MID_SECTION_HEIGH + BIN_BASE_BOTTOM_SECTION_HEIGH
BIN_MAGNET_HOLE_GROOVE_DEPTH = 0.06

BIN_LIP_EXTRA_HEIGHT = 0.44
BIN_LIP_WALL_THICKNESS = BIN_BASE_TOP_SECTION_HEIGH - BIN_XY_TOLERANCE
BIN_LIP_TOP_RECESS_HEIGHT = 0.06
BIN_WALL_THICKNESS = 0.12
BIN_CONNECTION_RECESS_DEPTH = 0.44
BIN_COMPARTMENT_BOTTOM_THICKNESS = 0.1
BIN_BODY_CUTOUT_BOTTOM_FILLET_RADIUS = 0.2

BIN_TAB_WIDTH = 1.3
BIN_TAB_OVERHANG_ANGLE = 45
BIN_TAB_EDGE_FILLET_RADIUS = 0.06

BIN_SCOOP_MAX_RADIUS = 2.5

BASEPLATE_EXTRA_HEIGHT = 0.64
BASEPLATE_BIN_Z_CLEARANCE = 0.05

DIMENSION_DEFAULT_WIDTH_UNIT = 4.2
DIMENSION_DEFAULT_HEIGHT_UNIT = 0.7
DIMENSION_SCREW_HOLES_DISTANCE = 3.0  # original 2.6, 1.6 is the wrong dirrection
DIMENSION_SCREW_HOLE_DIAMETER = 0.3
DIMENSION_PLATE_CONNECTION_SCREW_HOLE_DIAMETER = 0.32
DIMENSION_PLATE_SCREW_HOLE_DIAMETER = 0.32
DIMENSION_SCREW_HEAD_CUTOUT_DIAMETER = 0.6
DIMENSION_SCREW_HEAD_CUTOUT_OFFSET_HEIGHT = 0.05
DIMENSION_MAGNET_CUTOUT_DIAMETER = 0.65
DIMENSION_MAGNET_CUTOUT_DEPTH = 0.24
DIMENSION_PRINT_HELPER_GROOVE_DEPTH = 0.03


DEFAULT_FILTER_TOLERANCE = 0.00001