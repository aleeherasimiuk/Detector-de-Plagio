# Detector de Plagio

Trabajo Práctico realizado para la materia Procesamiento del Lenguaje Natural, de UTN-FRBA a cargo de Mg. Ing. Hernán Borré.

Objetivos:

- Detectar plagio entre trabajos prácticos de una materia
- Detectar plagio entre un trabajo práctico y la Web
- Detectar plagio entre un trabajo práctico y libros de la materia.

Herramientas y conceptos utilizados:

- Lemmatize
- Stemming
- Stop Words
- Latent Dirichlet Allocation
- Naive Bayes for Text Classification
- Word Embeddings
- Word Mover's Distance
- Named Entity Recognition
- Part of Speech
- Regular Expressions
- Unigrams/Bigrams/Trigrams
- Web Scrapping
- Topic Modeling
- Text Similarity

Librerías utilizadas:

- Textract
- Gensim
- Spacy
- NLTK
- Click
- Unittest
- Multiprocessing
- Pdfminer
- Python-pptx
- Docx
- Logging
- Firebase
- Pandas
- Numpy
- Scikit Learn
- Matplotlib
- Jupyter Notebooks

## Estructura del Proyecto

<pre>├── <font color="#729FCF"><b>books</b></font>
│   ├── La larga cola $ Chris_Anderson_La_economia_Long_Tail.pdf
│   ├── La nueva economia $ Kotler_P_and_Armstrong_G_2008_Fundamento.pdf
│   ├── La sociedad de costo marginal cero $ la sociedad de costo marginal cero.pdf
│   ├── Sistemas Emergentes $ Steven_Johnson_Sistemas_emergentes_O_que_tienen_en.pdf
│   └── Wikinomics $ Wikinomia.pdf
├── <font color="#729FCF"><b>data</b></font>
│   ├── accuracy.nv
│   ├── books.csv
│   ├── classes.nv
│   ├── class_probabilities.nv
│   ├── dataset.csv
│   ├── features_by_class.nv
│   ├── frequencies.nv
│   ├── lda_model
│   ├── lda_model2
│   ├── lda_model2.expElogbeta.npy
│   ├── lda_model2.id2word
│   ├── lda_model2.state
│   ├── lda_model.expElogbeta.npy
│   ├── lda_model.id2word
│   ├── lda_model.state
│   └── scrapped.csv
├── Detector de Plagio.pdf
├── <font color="#729FCF"><b>keyed_vectors</b></font>
│   ├── complete.kv
│   └── complete.kv.vectors.npy
├── <font color="#729FCF"><b>labeled_dataset</b></font>
│   
├── <font color="#729FCF"><b>logs</b></font>
├── LICENCE.md
├── README.md
├── <font color="#8AE234"><b>run.sh</b></font>
├── <font color="#8AE234"><b>run_tests.sh</b></font>
├── service_account_key.json
├── <font color="#729FCF"><b>src</b></font>
│   ├── document.py
│   ├── latent_dirichlet_allocation.ipynb
│   ├── main.py
│   ├── <font color="#729FCF"><b>models</b></font>
│   │   ├── lda_utils.py
│   │   ├── naive_bayes_utils.py
│   ├── naive_bayes.ipynb
│   ├── prepare_dataset.ipynb
│   ├── <font color="#729FCF"><b>__pycache__</b></font>
│   │   └── document.cpython-38.pyc
│   ├── <font color="#729FCF"><b>repository</b></font>
│   │   ├── csv_tools.py
│   │   ├── firebase_admin.py
│   │   ├── __init__.py
│   ├── scrapper.ipynb
│   ├── <font color="#729FCF"><b>tests</b></font>
│   │   ├── csv_tests.py
│   │   ├── data_processing_tests.py
│   │   ├── dictionary_tests.py
│   │   ├── file_manager_tests.py
│   │   ├── firebase_tests.py
│   │   ├── module_fix.py
│   │   ├── run_tests.py
│   │   └── text_extracting_tests.py
│   ├── <font color="#729FCF"><b>util</b></font>
│   │   ├── count_vectorizer.py
│   │   ├── data_cleaning.py
│   │   ├── doc2string.py
│   │   ├── exceptions.py
│   │   ├── file_manager.py
│   │   ├── generic_document.py
│   │   ├── <font color="#729FCF"><b>graphics</b></font>
│   │   │   ├── bar.py
│   │   │   ├── lda_triangle.py
│   │   │   └── word_cloud.py
│   │   ├── __init__.py
│   │   ├── log.py
│   │   ├── pdf2string.py
│   │   ├── ppt2string.py
│   │   ├── prompt_utils.py
│   │   └── scrapper.py
│   └── word_mover_distance.ipynb
└── <font color="#729FCF"><b>unit_testing_documents</b></font>
    ├── lorem_ipsum.doc
    ├── lorem_ipsum.docx
    ├── lorem_ipsum.pdf
    ├── lorem_ipsum.pptx
    └── lorem_ipsum.rtf
</pre>


## Output de ejemplo

<pre>Documentos para analizar:

	Documentos: 305
	Webs scrappeadas: 46
	Libros: 5


Potenciales nombres del alumno:

	- Posibilidad
	- ******** Rodrigo
	- Ley de Pareto


Analizando el tema del texto:

Naive Bayes -&gt; La larga cola  [98.36% de efectividad]

Latent Dirichlet Allocation -&gt; [largo cola ofrecer venta regla cliente demanda nicho oferta minorista] -&gt; [probabilidad del 97.05%]

Filtrando documentos por tema...

	Documentos a analizar: 50
	Textos scrappeados a analizar: 4
	Libros a analizar: 1

Presione una tecla para comenzar con el análisis de plagio.</pre>


<pre>Porcentaje de plagio: 48.64%
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">Párrafo plagio: [Párrafo #58]</font>
<font color="#4E9A06">Democratizar las herramientas de producción: La gente puede producir sin necesidad de acudir a profesionales, a diferencia de lo que sucedía tiempo atrás. Es posible editar video, convertir audio y realizar impresiones a color, entre muchas cosas, a un costo accesible y desde cualquier hogar.</font>



<font color="#4E9A06">Párrafo de referencia: [TP 1 - Marketing en Internet y Nueva Economía - Lucas ******.docx][Párrafo #49]</font>
<font color="#4E9A06"> La primera fuerza es democratizar las herramientas de producción. En consecuencia, el universo de contenidos disponibles ahora está creciendo con más rapidez que nunca. Esto es lo que extiende la larga cola hacia la derecha, multiplicando el número de bienes disponibles. Resultado: más productos, lo que extiende la larga cola.</font>


<font color="#4E9A06">Distancia: 2.0249130364836314</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">Párrafo plagio: [Párrafo #24]</font>
<font color="#4E9A06">La economía basada en el éxito, denominada de escasez, es la creación de una época en la que no había suficiente espacio para hacer que todo fuese accesible a todos: no había suficiente espacio de exhibición para todos los CD, DVD y videojuegos producidos; ni suficientes pantallas para proyectar todas las películas disponibles; ni suficientes canales para transmitir todos los programas de televisión; ni suficientes ondas hertzianas para emitir toda la música creada; ni tampoco había suficientes horas en el día para ofrecer todo a través de alguno de estos espacios. </font>



<font color="#4E9A06">Párrafo de referencia: [TP 1 - Marketing.docx][Párrafo #37]</font>
<font color="#4E9A06">Cuando la economía se basaba en el éxito, dado que no había suficiente espacio para que todo sea accesible a todos, cuando no había suficientes pantallas para proyectar todas las películas disponibles, ni suficientes canales para transmitir todos los programas de televisión, ni tampoco había suficientes horas del día para ofrecer todo a través de alguno de estos espacios, esto era la economía de la escasez.</font>


<font color="#4E9A06">Distancia: 1.4548918182908754</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">Párrafo plagio: [Párrafo #60]</font>
<font color="#4E9A06">Reducir los costos de consumo mediante la democratización de la distribución: Gracias al internet y los filtros que ofrecen las páginas al momento de realizar búsquedas, las recomendaciones automáticas y personalizadas para cada usuario, y las recomendaciones y reseñas hechas por otros que ya han comprado el producto que uno busca, se reducen los costos de consumo: Se encuentra lo que se busca más rápido, se encuentran bienes que satisfagan las necesidades de uno a menor precio (ya que las alternativas de nicho ahora son fácilmente encontrables), se evita la frustración de comprar algo que termine por no ser lo esperado, etc.</font>



<font color="#4E9A06">Párrafo de referencia: [Tp2 ****** marketing en internet (2).docx][Párrafo #32]</font>
<font color="#4E9A06">Democratizar las herramientas de producción, es decir poner al alcance de todos, todo. Reducir los costes de consumo mediante esta democratización, es decir que todos puedan actuar como productores, y publicarlo, hacerlo accesible al consumidor. La tercera fuerza es conectar la oferta con la demanda, orientando la demanda hacia la larga cola, y pudiendo ofrecer a los consumidores los productos. </font>


<font color="#4E9A06">Distancia: 1.954088581059449</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#4E9A06">Párrafo plagio: [Párrafo #9]</font>
<font color="#4E9A06">El seguimiento de las listas de productos más vendidos es una obsesión nacional. Nuestra cultura es una competición por la popularidad masiva. Nos fascinan los productos de gran éxito: fabricaros, elegirlos, hablar de ellos y contemplar su auge y decadencia.</font>



<font color="#4E9A06">Párrafo de referencia: [https://es.qaz.wiki/wiki/Long_tail][Párrafo #29]</font>
<font color="#4E9A06">Los factores del lado de la demanda que conducen a la cola larga pueden ser amplificados por las &quot;redes de productos&quot; que se crean mediante recomendaciones de hipervínculos entre productos. Un artículo de MIS Quarterly de Gal Oestreicher-Singer y Arun Sundararajan muestra que las categorías de libros en Amazon.com que son más centrales y, por lo tanto, están más influenciadas por su red de recomendaciones tienen distribuciones de cola larga significativamente más pronunciadas. Sus datos en 200 áreas temáticas muestran que duplicar esta influencia conduce a un aumento del 50% en los ingresos de la quinta parte de los libros menos populares. </font>


<font color="#4E9A06">Distancia: 1.9162861104791806</font>
<font color="#4E9A06">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#CC0000">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#CC0000">Párrafo plagio: [Párrafo #17]</font>
<font color="#CC0000">La larga estela o larga cola (en el original en inglés The Long Tail) fue una expresión popularizada por Chris Anderson en un artículo de la revista Wired de octubre de 2004 para describir determinados tipos de negocios y modelos económicos tales como Amazon o Netflix.1 2 Anderson elaboró el concepto en su libro The Long Tail: Why the Future of Business Is Selling Less of More.3 4 El término larga cola se utiliza normalmente en estadística en relación con distribuciones de riqueza o con el uso del vocabulario.</font>



<font color="#CC0000">Párrafo de referencia: [https://es.wikipedia.org/wiki/Larga_cola][Párrafo #0]</font>
<font color="#CC0000">La larga estela o larga cola (en el original en inglés The Long Tail) fue una expresión popularizada por Chris Anderson en un artículo de la revista Wired de octubre de 2004 para describir determinados tipos de negocios y modelos económicos tales como Amazon o Netflix.[1] [2] Anderson elaboró el concepto en su libro The Long Tail: Why the Future of Business Is Selling Less of More.[3] [4] El término larga cola se utiliza normalmente en estadística en relación con distribuciones de riqueza o con el uso del vocabulario. </font>


<font color="#CC0000">Distancia: 0.0</font>
<font color="#CC0000">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#C4A000">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
<font color="#C4A000">Oración plagio [Oración #5]</font>
<font color="#C4A000">Nos fascinan los productos de gran éxito: fabricaros, elegirlos, hablar de ellos y contemplar su auge y decadencia.</font>



<font color="#C4A000">Oración de referencia: [Chris_Anderson_La_economia_Long_Tail_TRUNCATED.pdf][Oración #455]</font>
<font color="#C4A000">Nos fascinan los productos de gran éxito: fabricarlos, elegirlos, hablar de ellos y contemplar su auge y decadencia.</font>


<font color="#C4A000">Distancia: 0.34250761071548874</font>
<font color="#C4A000">------------------------------------------------------------------------------------------------------------------------------------------------------</font>
</pre>


## Colores:
 - Rojo: Copiado
 - Amarillo: Similar
 - Verde: Parafraseo


# Referencias y tutoriales utilizados:

## Read Word Document: 

- https://grokonez.com/python/how-to-read-write-word-docx-files-in-python-docx-module


## Unit Testing in Python:

- https://docs.python.org/3/library/unittest.html


## Read Power Point Document:

- https://python-pptx.readthedocs.io/en/latest/


## Read PDF:

- https://pdfminersix.readthedocs.io/en/latest/

## Read Doc - RTF

- https://textract.readthedocs.io/en/stable/


## Logging:

- https://docs.python.org/3/howto/logging.html

## POS Tagging Spacy & NLTK

- https://www.i2tutorials.com/parts-of-speech-pos-tagging-with-nltk-and-spacy-using-python/


## Naive Bayes implementation

- https://medium.com/analytics-vidhya/naive-bayes-classifier-for-text-classification-556fabaf252b#:~:text=The%20Naive%20Bayes%20classifier%20is,time%20and%20less%20training%20data


## Firebase

- https://firebase.google.com/docs/firestore/quickstart

## Count Vectorizer

- https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.build_analyzer


## Tokenizing Sentences

- https://pythonspot.com/tokenizing-words-and-sentences-with-nltk/


## Name entity recognition:

- https://www.geeksforgeeks.org/python-named-entity-recognition-ner-using-spacy/?ref=rp


## Multiprocessing

- https://svitla.com/blog/parallel-computing-and-multiprocessing-in-python
- https://stackoverflow.com/questions/20664695/how-do-i-convert-a-multiprocessor-manager-list-to-a-pure-python-list
- https://medium.com/@lih.verma/multi-processing-in-python-process-vs-pool-5caf0f67eb2b
- https://docs.python.org/3/library/multiprocessing.html


## Triangle

- https://gist.github.com/tboggs/8778945
- http://blog.bogatron.net/blog/2014/02/02/visualizing-dirichlet-distributions/

# WMD

- https://radimrehurek.com/gensim/auto_examples/tutorials/run_wmd.html
- https://radimrehurek.com/gensim/auto_examples/tutorials/run_wmd.html#sphx-glr-download-auto-examples-tutorials-run-wmd-py
- https://towardsdatascience.com/word-movers-distance-for-text-similarity-7492aeca71b0
- https://markroxor.github.io/gensim/static/notebooks/WMD_tutorial.html


# Word Embeddings in Text Similarity

- https://medium.com/@Intellica.AI/comparison-of-different-word-embeddings-on-text-similarity-a-use-case-in-nlp-e83e08469c1c
- https://towardsdatascience.com/nlp-text-similarity-how-it-works-and-the-math-behind-it-a0fb90a05095
- https://pyshark.com/cosine-similarity-explained-using-python/
- https://arxiv.org/pdf/1405.4053v2.pdf
- https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.KeyedVectors.wmdistance
- https://zenodo.org/record/1410403
- https://github.com/aitoralmeida/spanish_word2vec
- https://morelab.deusto.es/datasets/info/word2vec-models-for-the-spanish-language/
- https://towardsdatascience.com/understanding-nlp-word-embeddings-text-vectorization-1a23744f7223


# Loading animation

- https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running

# Word Embeddings Model

Aitor Almeida, & Aritz Bilbao. (2018). Spanish 3B words Word2Vec Embeddings (Version 1.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1410403

Bilbao-Jayo, A., & Almeida, A. (2018). Automatic political discourse analysis with multi-scale convolutional neural networks and contextual data. International Journal of Distributed Sensor Networks, 14(11), 1550147718811827.
