swig -c++ -python .\win64\NLPIR.interface
copy .\win64\NLPIR.dll %SYSTEMROOT%\system32\ 
python setup.py build_ext --inplace
python setup.py install
pause