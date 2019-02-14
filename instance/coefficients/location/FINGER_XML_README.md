
These limits dictate when the actuator will be faulted. 
They should be within the JointMaxValue and JointMinValue to properly activate
    <Coeff id="JointSafety_LowerLimit_Rad" value="-1.14"/>
    <Coeff id="JointSafety_UpperLimit_Rad" value="4.7"/>


These limits are actually a range shift which converts the APS values that have a range of -pi to pi to be represented 
within these values.

SO. IT IS ABSOLUTELY IMPORTANT that JointMaxValue minus JointMinValue is a factor of 2PI.

    <Coeff id="JointMaxValue" value="-1.335"/>
    <Coeff id="JointMinValue" value="4.945"/>


Finally, IHMC assumes that an APS value of 0.0 is an open finger position and an APS value of up to  3.6 is a closed finger position
In other words, it takes at most 3.6 radians to close a finger. Thus, we have changed the limits above to reflect these assumptions.


 
