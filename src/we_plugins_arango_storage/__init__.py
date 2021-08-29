import logging
from arango import ArangoClient

log = logging.getLogger('we.plugins.arango_storage')


class ArangoStorage:
    """Arango storage workflow executor plugin."""
    def __init__(self, wm) -> None:
        """On creation workflow manager instance is passed."""
        conf_dict = wm.context.config.arango_storage._to_dict()

        log.debug(conf_dict)
        client = ArangoClient(hosts=conf_dict['hosts'])
        db = client.db(conf_dict['database'],
                       username=conf_dict['username'],
                       password=conf_dict['password'])

        self.db = db
        self.client = client


def db_connection(conf_dict):
    """Return python arango db connection based on config."""
    log.debug(conf_dict)
    client = ArangoClient(hosts=conf_dict['hosts'])
    db = client.db(conf_dict['database'],
                   username=conf_dict['username'],
                   password=conf_dict['password'])

    return client, db
