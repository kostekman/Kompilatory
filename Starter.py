import Parser as plyj

parser = plyj.Parser()

# parse a compilation unit from a file
tree = parser.parse_file(open('test.java'))

print(tree)
# parse a compilation unit from a string
#tree = parser.parse_string('class Foo { }')

# parse expression from string
#tree = parser.parse_expression('1 / 2 * (float) 3')
#
# slightly bigger example: parse from an installed JDK with sources
#import zipfile
#srczip = zipfile.ZipFile('/usr/lib/jvm/java-6-openjdk/src.zip', mode='r')
#info = srczip.getinfo('java/lang/Object.java')
#srcfile = srczip.open(info)
#tree = parser.parse_file(srcfile)
