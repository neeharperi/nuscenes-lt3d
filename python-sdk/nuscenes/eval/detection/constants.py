# nuScenes dev-kit.
# Code written by Oscar Beijbom and Varun Bankiti, 2019.

DETECTION_NAMES = ['car', 'truck', 'trailer', 'bus', 'construction_vehicle', 'bicycle', 'motorcycle', 'emergency_vehicle',
                  'adult', 'child', 'police_officer', 'construction_worker', 'stroller', 'personal_mobility', 
                  'pushable_pullable', 'debris', 'traffic_cone', 'barrier']

PRETTY_DETECTION_NAMES = {
    'bus': 'Bus',
    'car': 'Car',
    'trailer': 'Trailer',
    'truck': 'Truck',
    'construction_vehicle': 'Construction Vehicle',
    'emergency_vehicle': 'Emergency Vehicle',
    'adult': 'Adult',
    'child': 'Child',
    'police_officer': 'Police Officer',
    'construction_worker': 'Construction Worker',
    'personal_mobility': 'Personal Mobility',
    'motorcycle': 'Motorcycle',
    'bicycle': 'Bicycle',
    'pushable_pullable': 'Pushable Pullable',
    'stroller': 'Stroller',
    'traffic_cone': 'Traffic Cone',
    'barrier': 'Barrier',
    'debris' : 'Debris',
}

DETECTION_COLORS = {
    'bus': 'C0',
    'car': 'C1',
    'trailer': 'C2',
    'truck': 'C3',
    'construction_vehicle': 'C4',
    'emergency_vehicle': 'C5',
    'adult': 'C6',
    'child': 'C7',
    'police_officer': 'C8',
    'construction_worker': 'C9',
    'personal_mobility': 'C0',
    'motorcycle': 'C1',
    'bicycle': 'C2',
    'pushable_pullable': 'C3',
    'stroller': 'C4',
    'traffic_cone': 'C5',
    'barrier': 'C6',
    'debris' : 'C7',
                    }

ATTRIBUTE_NAMES = ['pedestrian.moving', 'pedestrian.sitting_lying_down', 'pedestrian.standing', 'cycle.with_rider',
                   'cycle.without_rider', 'vehicle.moving', 'vehicle.parked', 'vehicle.stopped']

PRETTY_ATTRIBUTE_NAMES = {'pedestrian.moving': 'Ped. Moving',
                          'pedestrian.sitting_lying_down': 'Ped. Sitting',
                          'pedestrian.standing': 'Ped. Standing',
                          'cycle.with_rider': 'Cycle w/ Rider',
                          'cycle.without_rider': 'Cycle w/o Rider',
                          'vehicle.moving': 'Veh. Moving',
                          'vehicle.parked': 'Veh. Parked',
                          'vehicle.stopped': 'Veh. Stopped'}

TP_METRICS = ['trans_err', 'scale_err', 'orient_err', 'vel_err', 'attr_err']

PRETTY_TP_METRICS = {'trans_err': 'Trans.', 'scale_err': 'Scale', 'orient_err': 'Orient.', 'vel_err': 'Vel.',
                     'attr_err': 'Attr.'}

TP_METRICS_UNITS = {'trans_err': 'm',
                    'scale_err': '1-IOU',
                    'orient_err': 'rad.',
                    'vel_err': 'm/s',
                    'attr_err': '1-acc.'}
