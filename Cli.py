import cmd
import Ya


class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro = "Hi!\nWrite 'help' to get commands\nRewrite your TOKEN with command 'token'"
        self.doc_header = "Avaliable commands (for help to the command write: help 'command')"

    def do_token(self, args):
        '''rewrite token'''
        print('Input your token')
        token = input()
        Ya.TOKEN = token

    def do_upload(self, args):
        '''download file or dirrectory'''
        print('Input file/dir')
        file = input()
        Ya.upload_file(file, file)

    def do_mkDir(self, args):
        '''create dirrectory'''
        print('Input dir name')
        dir = input()
        Ya.mkDir(dir)

    def do_listed(self, args):
        '''list of file on disk'''
        list = Ya.listed()
        for x in list:
            print(x)

    def do_download(self, args):
        '''download file or directory'''
        print('Input file/dir name')
        path = input()
        Ya.download(path)

    def do_remove(self, args):
        '''remove file or dirrectiry'''
        print('Input file/dir name')
        path = input()
        Ya.remove(path)


if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("The end")
