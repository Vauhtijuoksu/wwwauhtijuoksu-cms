from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool



class UserToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu( 'vj-cms-user-toolbar', 'Käyttäjä')

        menu.add_link_item(
            name='Vaihda salasana',
            url='/accounts/password/change/',
        )
        menu.add_link_item(
            name='Kirjaudu ulos',
            url='/accounts/logout/',
        )

# register the toolbar
toolbar_pool.register(UserToolbar)
