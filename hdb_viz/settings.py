from pydantic import BaseSettings

from hdb_viz.constants import Page


class Settings(BaseSettings):

    default_page: Page = Page.UPLOAD_DATASET
