class TrueSkillPredictor(object):

    def __init__(self, datastore):
        self.datastore = datastore

    def predict(self, blue_alliance: list, red_alliance: list):
        """Returns the likelihood of each alliance winning."""
        return (0.5, 0.5)

    def update(self, match_key: str):
        pass
