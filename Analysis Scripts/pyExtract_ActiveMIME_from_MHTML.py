'''
    OLE Extraction from MHTML
    by Jacob Soo Lead Re

    Hashes for samples:
    e2f45f24ecbb65db5b6e26389bb55e8919706a0c6a087c8fa7afe532be9b8dfd
    4ffc062316fe2e6187d23ac32e3987b3443c623b0686124d22010a42b60f9a8a
    4f16b83bbaf9b7b77966591e59e07a7d9c61f5fe1de82bcfc521294cc0711727
    8f55abf50281603ad0af7f450e4eabc048e8763a56f1f7851dd874776628cd64
    c111a7dbe059c72f55d06f662154caa0483721577cd19e9e9e6362a5c44fd02f
'''

__author__ = "Jacob Soo Lead Re"
__version__ = "0.1"

import zlib
import base64
import re
import sys

def _log(szString):
    print(szString)

def extractZLibData(data):
    if not re.match("ActiveMime", data):
        return ""
    found = re.search('\x78\x9c', data,re.MULTILINE)
    if found:
        return data[found.start():len(data)]

def extractOLE(szFilePath):
    ole = ""
    hFile = file(szFilePath,"rb")
    dataRead = hFile.read()
    hFile.close()
    
    found = re.search("^Content-Location:\x20file:///[^\n]{0,999}?editdata\.mso.*?\r\n\r\n^((?:[A-Za-z0-9+/\r\n]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)\r\n", dataRead, re.DOTALL|re.MULTILINE|re.IGNORECASE)
    if found:
        ole = found.group(1)
    return ole

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        _log("[+] Usage: %s [MHTML_Containing_MIME]" % sys.argv[0])
        sys.exit(0)
    else:
        _log("[+] Find ActiveMIME from %s" % sys.argv[1])
        g = extractOLE(sys.argv[1])
        if g:
            _log("[+] ActiveMIME found!")
            activemimestream = base64.b64decode(g)
            if activemimestream:
                _log("[+] Extracting OLE now!")
                zlibdata = extractZLibData(activemimestream)
                olestream = zlib.decompress(zlibdata)
                hFile = file(sys.argv[1]+".ole", "wb")
                hFile.write(olestream)
                hFile.close()
                _log("[+] OLE file extracted to %s.ole\n" % sys.argv[1])
            else:
                _log("[-] ActiveMIME seems corrupted!")
        else:
            _log("[-] ActiveMIME not found!")
            
