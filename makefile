
all: run

run: dtTree astTree
	
astTree:
	python3 ASTParser.py
	dot -Tjpeg saida.dot -o AST.jpg
	
dtTree:
	echo "AQUI"
	python3 DTParser.py
	dot -Tjpeg saida.dot -o DT.jpg
cleanCache:
	rm -rd __pycache__
clean: cleanCache
