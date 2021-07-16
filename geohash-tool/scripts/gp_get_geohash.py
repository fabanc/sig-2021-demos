import arcpy


def process(feature_class, field, precision=8):

    with arcpy.da.UpdateCursor(feature_class, ['SHAPE@', field]) as cursor:
        for row in cursor:
            geom = row[0]
            geohash = geom.getGeohash(precision)
            row[1] = geohash
            cursor.updateRow(row)
    return


if __name__ == '__main__':
    process(
        feature_class=arcpy.GetParameterAsText(0),
        field=arcpy.GetParameterAsText(1)
    )