# by m4ll0k - github.com/m4ll0k

import requests
from jsbeautifier import beautify
import sys, re
import string
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
blacklisted = [
    "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "enum", "break",
    "export", "extends", "false", "finally", "for", "function", "if", "implements", "import", "in", "instanceof",
    "interface", "let", "new", "null", "package", "private", "protected", "public", "return", "super",
    "switch", "static", "this", "throw", "try", "true", "typeof", "var", "void", "while", "with", "abstract", "else",
    "instanceof", "super", "boolean", "enum", "int", "switch", "break", "export", "interface", "synchronized", "byte",
    "extends", "let", "this", "case", "false", "long", "throw", "catch", "final", "native", "await",
    "throws", "char", "finally", "new", "transient", "class", "float", "null", "true", "const", "case",
    "for", "package", "try", "continue", "function", "private", "typeof", "debugger", "goto", "protected", "var",
    "default", "if", "public", "void", "delete", "implements", "return", "volatile", "do", "import", "short",
    "while", "double", "in", "static", "with", "alert", "frames", "outerheight", "all", "framerate", "outerwidth",
    "anchor", "function", "packages", "anchors", "getclass", "pagexoffset", "area", "hasownproperty",
    "pageyoffset", "array", "hidden", "parent", "assign", "history", "parsefloat", "blur", "image", "parseint",
    "password", "checkbox", "infinity", "pkcs11", "clearinterval", "isfinite", "plugin", "cleartimeout", "isnan",
    "clientinformation", "isprototypeof", "propertyisenum", "prompt", "button", "images",
    "close", "java", "prototype", "closed", "javaarray", "radio", "confirm", "javaclass", "reset", "constructor",
    "screenx", "crypto", "javapackage", "screeny", "date", "defaultstatus", "javaobject",
    "innerheight", "scroll", "decodeuri", "innerwidth", "secure", "decodeuricomponent", "layer", "select",
    "layers", "self", "document", "length", "setinterval", "element", "link", "settimeout", "elements", "location",
    "status", "embed", "math", "string", "embeds", "mimetypes", "submit", "encodeuri", "name",
    "taint", "encodeuricomponent", "nan", "text", "escape", "navigate", "textarea", "eval", "navigator", "top", "event",
    "number", "tostring", "fileupload", "object", "undefined", "focus", "offscreenbuffering", "unescape", "form",
    "open", "untaint", "forms", "opener", "valueof", "frame", "option", "window", "yield",
]


def getWords(content):
    """ Searching word in Js file """
    allWords = []
    content = beautify(content)
    regex_content = re.findall(r'[a-zA-Z0-9_\-.]+', content, re.I)
    for word in regex_content:
        if '.' in word:
            w = word.split('.')[-1:][0]
            if w and w not in allWords:
                allWords.append(w)
        elif len(word) == 1:
            if word in string.punctuation:
                pass
            elif word in string.ascii_letters:
                if word not in allWords:
                    allWords.append(word)
            elif word in string.digits:
                pass
        else:
            if word not in allWords:
                allWords.append(word)
    F_allWords = []
    for word_ in allWords:
        if word_.lower() not in blacklisted:
            if word_ not in F_allWords:
                F_allWords.append(word_)
    return F_allWords


def doMyWork(jsFile):
    """ Download Js file and parse them to search some word """
    if '://' in jsFile and '.js' in jsFile:
        try:
            req = requests.get(jsFile, verify=False)
            if req.status_code == 200:
                words = getWords(req.content.decode('utf-8', 'replace'))
                for word in words:
                    print(word)
        except Exception as err:
            sys.exit(print(err))
    else:
        print("Bad JsFile" + jsFile)


if __name__ == "__main__":
    """ Choose if the input is from stdin or argv """
    stdin = False
    if len(sys.argv) == 2:  # took from argv
        doMyWork(sys.argv[1])
    else:
        for stdinJsFile in sys.stdin.readlines():  # took from stdin
            doMyWork(stdinJsFile.strip())
