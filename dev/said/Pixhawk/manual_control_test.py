import unittest
from unittest.mock import MagicMock, patch
from your_module_name import arm_and_control_vehicle

class TestArmAndControlVehicle(unittest.TestCase):

    @patch('your_module_name.mavutil')
    @patch('time.sleep', MagicMock())
    def test_arm_and_control_vehicle(self, mock_mavutil):
        # Mocking mavutil.mavlink_connection
        mock_connection = MagicMock()
        mock_mavutil.mavlink_connection.return_value = mock_connection

        # Mocking motors_armed_wait
        mock_connection.motors_armed_wait.return_value = None

        arm_and_control_vehicle('/dev/test_port')

        # Assertions
        mock_mavutil.mavlink_connection.assert_called_once_with('/dev/test_port', baud=115200)
        mock_connection.wait_heartbeat.assert_called_once()
        mock_connection.mav.command_long_send.assert_called_once_with(
            mock_connection.target_system,
            mock_connection.target_component,
            mock_mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1, 0, 0, 0, 0, 0, 0
        )
        mock_connection.motors_armed_wait.assert_called_once()
        self.assertTrue(mock_connection.mav.manual_control_send.called)
        self.assertTrue(mock_connection.close.called)

if __name__ == '__main__':
    unittest.main()
