# -*- coding: utf-8 -*-
__author__ = 'Sangjin'

'''x-windows-949 에러시 PyCharm Settings - File Editor - File Encoding 에서 UTF-8로 모두 변경'''

import urllib2  # URL을 받아오기 위해 urllib2 라이브러리 Import
import os.path  # 파일 검사를 위해 os 라이브러리 Import


if not os.path.exists("rss.xml"): # 파일이 없을경우 만들기
    url = urllib2.urlopen("http://rss.etnews.com/Section04.xml").read()
    f = open('rss.xml', 'w')
    f.write(url)
    f.close()
else: # 파일이 있을 경우
    url = urllib2.urlopen("http://rss.etnews.com/Section04.xml").read()
    f1 = open('rss.xml', 'w')
    if f1 != url: # 기존 rss.xml 과 비교하여 동일하지 않을때
        url = urllib2.urlopen("http://rss.etnews.com/Section04.xml").read()
        f2 = open('rss.xml', 'w')
        f2.write(url)  # REMOTE URL XML 읽은 내용을 로컬 XML에 쓰기
        f2.close()  # 파일 닫기
    else:
        pass # 동일하면 pass

from xml.etree.ElementTree import parse  # ElementTree XML Parser Import

fp = parse("rss.xml")
root = fp.getroot() # 문서 최상단 변수
channel = root.find("channel") # 문서 최상단 아래 자식검색

print "[XML 문서 제목출력]"
print "-------------------------------------------------------"
for element in root.findall("channel"): # 문서최상단 아래 자식에서 Element 검색
    print element.findtext("title") # 타이틀 출력
    print element.findtext("link") # 링크 출력
    print element.findtext("description") # 설명 출력
    print "-------------------------------------------------------"

for element in channel.findall("item"): # 자식에서 item 내 element 검색
    print element.findtext("title") # 타이틀 출력
    print element.findtext("link") # 링크 출력