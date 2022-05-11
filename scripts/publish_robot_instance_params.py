#!/bin/env python

from logging import exception
import rospy
import argparse
import sys
import xmltodict

def load_params(instance_file, prefix):
    """Load parameters from an instance file to the parameter server under the given prefix.

    Args:
        instance_file (str): path to the robot instance file
        prefix (str): rosparam prefix to use for instance parameters
    """

    try:
        xml_params = open(instance_file).read()
        xml_params_dict = xmltodict.parse(xml_params, attr_prefix='', cdata_key='text', dict_constructor=dict)
    except Exception as e:
        rospy.logerr("Unable to load XML instance file: " + str(e))
        sys.exit(1)

    try:
        rospy.set_param(prefix, xml_params_dict)
    except rospy.ROSException as e:
        rospy.logerr("Unable to set instance parameters on the param server: " + str(e))

    rospy.loginfo("Loaded params from {0} to the parameter server successfully".format(instance_file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instance-file", required=True, help="Path to an XML instance file")
    parser.add_argument("-p", "--prefix", default="/valkyrie/instance", help="Parameter server prefix for instance params")
    args = parser.parse_args(sys.argv[1:])
    rospy.init_node(name="publish_robot_instance_params", anonymous=True)
    rospy.loginfo("Got instance file: " + args.instance_file)
    rospy.loginfo("Got prefix: " + args.prefix)
    load_params(args.instance_file, args.prefix)