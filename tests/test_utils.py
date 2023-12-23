import unittest
from unittest.mock import patch, Mock
from your_module import run_sql_query  # Replace 'your_module' with the actual module name

class TestRunSqlQuery(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_run_sql_query_success(self, mock_connect):
        # Mocking the cursor and connection
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Define connection parameters and SQL query
        connection_params = {
            'dbname': 'your_db',
            'user': 'your_user',
            'password': 'your_password',
            'host': 'your_host',
            'port': 'your_port'
        }
        query = "SELECT * FROM your_table;"

        # Call the function
        run_sql_query(connection_params, query)

        # Assertions
        mock_connect.assert_called_once_with(**connection_params)
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.commit.assert_called_once()
        mock_connect.return_value.close.assert_called_once()

    @patch('psycopg2.connect')
    def test_run_sql_query_error(self, mock_connect):
        # Mocking the cursor and connection to raise an exception
        mock_cursor = Mock()
        mock_cursor.execute.side_effect = Exception("Test error")
        mock_connect.return_value.cursor.return_value = mock_cursor

        # Define connection parameters and SQL query
        connection_params = {
            'dbname': 'your_db',
            'user': 'your_user',
            'password': 'your_password',
            'host': 'your_host',
            'port': 'your_port'
        }
        query = "SELECT * FROM your_table;"

        # Call the function
        run_sql_query(connection_params, query)

        # Assertions
        mock_connect.assert_called_once_with(**connection_params)
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.close.assert_called_once()
        mock_connect.return_value.commit.assert_not_called()  # No commit in case of an error
        mock_connect.return_value.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
