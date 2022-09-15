class ValidateCoordinatesCommand:
    rows = None
    columns = None
    row_coordinate = None
    column_coordinate = None

    def __init__(self, rows, columns, row_coordinate, column_coordinate):
        self.rows = rows
        self.columns = columns
        self.row_coordinate = row_coordinate
        self.column_coordinate = column_coordinate

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_row_coordinate(self):
        return self.row_coordinate

    def get_column_coordinate(self):
        return self.column_coordinate
