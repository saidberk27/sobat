import rospy
from rospy.srv import multiplier, multiplierResponse

def callback(request):
    return multiplierResponse(request.a, request.b)

def multiply():
    rospy.init_node()
    service = rospy.Service("multiplier", multiplier, callback)
    rospy.spin()

if __name__ == "__main__":
    multiply()