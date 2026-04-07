from page_factory.component import Component


class InfoField(Component):
    @property
    def type_of(self) -> str:
        return 'infofield'