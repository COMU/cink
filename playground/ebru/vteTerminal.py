import gtk
import vte
import os
import gobject

class VteTerminal():
        def constr(self):
                self.terminal = []
                self.index_ = -1

        def terminal_setting(self):
                self.argv = ['bash']
                self.env = self.env_map_to_list(os.environ.copy())
                self.cwd = os.environ['HOME']
                self.is_fullscreen = False
                self.terminal.append(vte.Terminal())
                # self.index_ sekme sayfasiyla ayni
#                self.terminal[self.index_].set_colors(gtk.gdk.color_parse('white'),gtk.gdk.color_parse('pink'),[])
		self.terminal[self.index_].set_opacity(0)

        def terminal_action(self):
                self.terminal[self.index_].fork_command(self.argv[0], self.argv, self.env, self.cwd)
                return self.terminal[self.index_]

        def env_map_to_list(self, env): # terminal fork_command icin
                return ['%s=%s' % (k, v) for (k, v) in env.items()]

