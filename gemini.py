import os,subprocess
from urllib.parse import urljoin

def start_response(meta,code="20"):
	print(f"{code} {meta}",end="\r\n")

def get_input():
	return os.environ.get("QUERY_STRING","")

# utility func
def has_input():
	return bool(get_input())

def link(text,url):
	print(f"=> {url} {text}")

def header(text,level=1):
	print("#"*level + " " + text)

# named for convenience; in practice just use header func with different levels
def h1(text):
	header(text,1)

def h2(text):
	header(text,2)

def h3(text):
	header(text,3)

def text(text=""):
	print(text)

def figlet(tex,**opts):
	if len(opts.keys())==0:
		opts = {"f":"standard"}
	ct = ["/usr/bin/figlet"]
	for k in opts:
		ct.append("-"+k)
		ct.append(opts[k])
	ct.append(tex)
	text("```")
	command_out(ct)
	text("```")

def command_lines(ct):
	for l in subprocess.check_output(ct).decode("ascii").split("\n"):
		yield l

def command_out(ct,f=text):
	for l in command_lines(ct):
		f(l)

def has_client_cert():
	return os.environ.get("AUTH_TYPE","")=="Certificate"

def get_client_cert():
	return os.environ["TLS_CLIENT_HASH"]

def get_remote_user():
	return os.environ.get("REMOTE_USER",os.environ["TLS_CLIENT_SUBJECT_CN"])
