import unittest
from unittest.mock import MagicMock, patch
from manual_control import ManualControl

class TestManualControl(unittest.TestCase):

    @patch('manual_control.mavutil.mavlink_connection')
    def test_getHeartBeat(self, mock_mavlink_connection):
        manual_control_instance = ManualControl(pixhawk_port='/dev/ttyACM0', motor_hiz=750)
        manual_control_instance.getHeartBeat()
        mock_mavlink_connection.assert_called_once_with('/dev/ttyACM0', baud=115200)
        mock_mavlink_connection.return_value.wait_heartbeat.assert_called_once()

    @patch('manual_control.mavutil.mavlink_connection')
    def test_armPixHawk(self, mock_mavlink_connection):
        mock_master = MagicMock()
        mock_mavlink_connection.return_value = mock_master

        manual_control_instance = ManualControl(pixhawk_port='/dev/ttyACM0', motor_hiz=750)
        manual_control_instance.armPixHawk()


        mock_master.motors_armed_wait.assert_called_once()

    @patch('manual_control.mavutil.mavlink_connection')
    @patch('time.sleep', MagicMock())
    def test_thrustMotors(self, mock_mavlink_connection):
        mock_master = MagicMock()
        mock_mavlink_connection.return_value = mock_master

        manual_control_instance = ManualControl(pixhawk_port='/dev/ttyACM0', motor_hiz=750)
        manual_control_instance.thrustMotors()

        mock_master.mav.manual_control_send.assert_called_once_with(
            mock_master.target_system,
            manual_control_instance.motor_hiz,
            0,
            0,
            0,
            0
        )
        mock_master.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
