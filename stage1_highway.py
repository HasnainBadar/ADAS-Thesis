from scenariogeneration import xodr
import os

def make_lane(lane_type, width, rm=xodr.RoadMarkType.broken):
    lane = xodr.Lane(lane_type=lane_type)
    lane.add_lane_width(width)
    lane.add_roadmark(xodr.RoadMark(rm))
    return lane

def build_highway_lanes():
    center = xodr.Lane()
    center.add_roadmark(xodr.RoadMark(xodr.RoadMarkType.solid))
    ls = xodr.LaneSection(0, center)
    ls.add_left_lane(make_lane(xodr.LaneType.driving, 3.75))
    ls.add_left_lane(make_lane(xodr.LaneType.driving, 3.75, xodr.RoadMarkType.solid))
    ls.add_left_lane(make_lane(xodr.LaneType.shoulder, 3.0, xodr.RoadMarkType.solid))
    ls.add_right_lane(make_lane(xodr.LaneType.driving, 3.75))
    ls.add_right_lane(make_lane(xodr.LaneType.driving, 3.75, xodr.RoadMarkType.solid))
    ls.add_right_lane(make_lane(xodr.LaneType.shoulder, 3.0, xodr.RoadMarkType.solid))
    lanes = xodr.Lanes()
    lanes.add_lanesection(ls)
    return lanes

pv = xodr.PlanView(0, 0, 0)
pv.add_geometry(xodr.Line(500))
highway = xodr.Road(0, pv, build_highway_lanes(), name="A270_Highway")
odr = xodr.OpenDrive("ADAS_Map1")
odr.add_road(highway)
odr.adjust_roads_and_lanes()
os.makedirs("map", exist_ok=True)
odr.write_xml("map/map1_stage1.xodr")
print("map1_stage1.xodr written")