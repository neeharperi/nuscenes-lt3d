# nuScenes dev-kit.
# Code written by Holger Caesar, 2018.

from typing import List, Optional


def category_to_detection_name(category_name: str) -> Optional[str]:
    """
    Default label mapping from nuScenes to nuScenes detection classes.
    Note that pedestrian does not include personal_mobility, stroller and wheelchair.
    :param category_name: Generic nuScenes class.
    :return: nuScenes detection class.
    """
    detection_mapping = {
        "vehicle.car": "car", 
        "vehicle.bus.bendy": "bus", 
        "vehicle.bus.rigid": "bus", 
        "vehicle.truck": "truck", 
        "vehicle.construction": "construction_vehicle",
        "vehicle.emergency.ambulance": "emergency_vehicle", 
        "vehicle.emergency.police": "emergency_vehicle", 
        "vehicle.trailer": "trailer", 
        "vehicle.motorcycle": "motorcycle", 
        "vehicle.bicycle": "bicycle", 

        "human.pedestrian.adult": "adult", 
        "human.pedestrian.child": "child", 
        "human.pedestrian.police_officer": "police_officer", 
        "human.pedestrian.construction_worker": "construction_worker", 
        "human.pedestrian.personal_mobility": "personal_mobility", 
        "human.pedestrian.wheelchair": "ignore",
        "human.pedestrian.stroller": "stroller",


        "movable_object.pushable_pullable": "pushable_pullable",
        "movable_object.debris": "debris", 
        "movable_object.barrier": "barrier", 
        "movable_object.trafficcone": "traffic_cone", 
    }

    if category_name in detection_mapping:
        return detection_mapping[category_name]
    else:
        return None


def detection_name_to_rel_attributes(detection_name: str) -> List[str]:
    """
    Returns a list of relevant attributes for a given detection class.
    :param detection_name: The detection class.
    :return: List of relevant attributes.
    """
    if detection_name in ['pedestrian']:
        rel_attributes = ['pedestrian.moving', 'pedestrian.sitting_lying_down', 'pedestrian.standing']
    elif detection_name in ['bicycle', 'motorcycle']:
        rel_attributes = ['cycle.with_rider', 'cycle.without_rider']
    elif detection_name in ['car', 'bus', 'construction_vehicle', 'trailer', 'truck']:
        rel_attributes = ['vehicle.moving', 'vehicle.parked', 'vehicle.stopped']
    elif detection_name in ['barrier', 'traffic_cone']:
        # Classes without attributes: barrier, traffic_cone.
        rel_attributes = []
    else:
        raise ValueError('Error: %s is not a valid detection class.' % detection_name)

    return rel_attributes

