## Logging and Exception handelling

* Outline: 
    - In ``src`` Make ``components``
    - In ``src`` make ``pipeline``


1. In ``src`` Make ``components``
    - 1.1: Make the folder
    - 1.2: In components, make ``__init__.py``
        * This is because we want the components to be in the form of a package. 
        * It will have all the modules. Ex: data-ingestion, data-transformation, data-validation, ...

    - 1.3: Make the module files. 
        * data_ingestion: Reading the data
        * data_transformation: Transforming the data
        * model_trainer: training the model 

2. In ``src`` make ``pipeline``:
    ``pipeline``is a way of organizing a series of operations or functions that process some data. 

    - 2.1: Make the ``train_pipeline.py`` in the folder
    - 2.2: Make the ``perdict_pipeline.py`` in the folder
    - 2.3: Make the ``__init__.py`` in the folder so we can import it. 