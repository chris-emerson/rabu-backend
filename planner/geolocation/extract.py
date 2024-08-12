def extract_placename(feature_collection):
    """Return the place name of the first result.

    Keyword arguments::
    feature_collection -- Query results from a MapBox Search result
    """
    return feature_collection['features'][0]['place_name']


def extract_coordinates(feature_collection):
    """Return the coordinates of the first result.

    Keyword arguments:
    feature_collection -- Query results from a MapBox Search result
    """
    return feature_collection['features'][0]['properties']['coordinates']