# DataMining-Examen

## Corrección del examen de la clase de Data Mining 202520 - NRC 2713

### Parte Teórica

**1) ¿Qué afirmación describe mejor por qué un contenedor es "más ligero" que una VM?**

* A. Incluye su propio kernel y drivers, pero comparte el filesystem con el host
* **B. Comparte el kernel del host y aísla procesos con mecanismos del SO**
* C. Ejecuta un hipervisor dentro del contenedor para virtualizar CPU
* D. Compila el código a binario estático antes de correr el proceso

> **Respuesta correcta:** B

---

**2) (Seleccionar las verdaderas) Sobre imágenes Docker y capas (layers), ¿cuáles enunciados son correctos?**

* **A. Las imágenes se componen de capas reutilizables entre builds**
* **B. Las capas de imagen son inmutables; el contenedor agrega una capa de escritura**
* C. Cada RUN del Dockerfile siempre sobrescribe la capa anterior sin crear nuevas capas
* **D. Copy-on-write permite eficiencia al modificar archivos sin duplicar toda la imagen**

> **Respuestas correctas:** A, B, D

---

**3) ¿Cuál es el riesgo principal de usar `latest` en producción?**

* A. Impide hacer pull desde registries privados
* B. Hace que el contenedor no pueda exponer puertos
* **C. Introduce cambios no deterministas y rompe trazabilidad de despliegues**
* D. Aumenta automáticamente permisos del contenedor

> **Respuesta correcta:** C

---

**4) En Docker Compose, ¿qué diferencia es crítica entre `depends_on` y un `healthcheck`?**

* A. `depends_on` garantiza que el servicio está listo para aceptar conexiones
* B. `healthcheck` solo sirve para logging; no impacta readiness
* **C. `depends_on` define orden de arranque; `healthcheck` valida salud real del servicio**
* D. Son equivalentes si se usa `restart: always`

> **Respuesta correcta:** C

---

**5) (Seleccionar las verdaderas) En la comparación Kubernetes vs Docker, ¿qué afirmaciones son coherentes?**

* **A. Docker es principalmente runtime/build de contenedores; Kubernetes orquesta despliegue y operación**
* B. Kubernetes reemplaza completamente la necesidad de imágenes Docker
* **C. Kubernetes aporta scheduling, auto-healing, escalado y service discovery**
* D. Docker Compose y Kubernetes cumplen exactamente el mismo rol en ambientes productivos multinodo

> **Respuestas correctas:** A, C

---

**6) ¿Qué definición distingue mejor "orquestación" de "automatización"?**

* A. Son sinónimos; solo cambia el nombre de la herramienta
* **B. Automatización ejecuta tareas; orquestación coordina dependencias, estado, retries y observabilidad end-to-end**
* C. Orquestación aplica solo a streaming; automatización solo a batch
* D. Orquestación elimina la necesidad de DAGS

> **Respuesta correcta:** B

---

**7) En un DAG de orquestación, ¿qué propiedad debe cumplirse?**

* A. Puede tener ciclos si se definen "retries"
* **B. Debe ser acíclico; no puede contener ciclos de dependencias**
* C. Cada tarea debe depender de todas las tareas anteriores
* D. Solo puede ejecutarse mediante cron

> **Respuesta correcta:** B

---

**8) (Seleccionar las verdaderas) Respecto a backfill/catchup y diseño idempotente:**

* **A. Un backfill recomputa ventanas pasadas por correcciones o cambios**
* **B. Catchup ejecuta corridas pendientes por fechas programadas no ejecutadas**
* **C. Idempotencia implica que reejecutar una ventana/lote no duplica datos**
* D. La idempotencia se logra únicamente desactivando retries

> **Respuestas correctas:** A, B, C

---

**9) ¿Qué diseño reduce mejor el riesgo de duplicados con reintentos?**

* A. Usar append siempre, sin llaves, porque es más rápido
* B. Full refresh de todo el histórico en cada corrida
* **C. Idempotencia por partición/ventana + upsert/merge cuando apliques**
* D. Desactivar reintentos y confiar en ejecuciones manuales

> **Respuesta correcta:** C

---

**10) (Seleccionar las verdaderas) ¿Cuáles elementos son más consistentes con "observabilidad" en pipelines?**

* **A. Métricas de duración, throughput, éxito/falla por tarea**
* **B. Alertas accionables con contexto (qué falló, impacto, próxima acción)**
* C. Únicamente logs sin métricas ni estados
* **D. Lineage/metadata para rastrear origen y transformaciones**

> **Respuestas correctas:** A, B, D

---

**11) ¿Cuál afirmación describe mejor un Data Warehouse moderno (OLAP) en la nube?**

* A. Diseñado para transacciones OLTP de baja latencia
* **B. Diseñado para análisis, datos históricos y gobernanza; frecuentemente separa compute y storage**
* C. Diseñado para eliminar necesidad de modelado y semántica
* D. Diseñado para ejecutar únicamente sobre CSV planos sin esquema

> **Respuesta correcta:** B

---

**12) ¿Qué diferencia resume mejor ETL vs ELT en cloud?**

* A. ETL transforma dentro del DWH; ELT transforma antes de cargar
* **B. ETL transforma antes de cargar; ELT carga crudo y transforma dentro del warehouse/lakehouse**
* C. Son equivalentes; solo cambia la herramienta
* D. ELT elimina la necesidad de SQL, o transformaciones

> **Respuesta correcta:** B

---

**13) (Seleccionar las verdaderas) "Pruning/data skipping" es importante porque:**

* **A. Permite omitir particiones/bloques irrelevantes y reducir datos escaneados**
* **B. Reduce costo y tiempo al evitar leer datos innecesarios**
* C. Solo funciona si hay índices B-tree como en OLTP
* **D. Depende fuertemente de metadatos/estadísticas (particiones, min/max, manifiestos)**

> **Respuestas correctas:** A, B, D

---

**14) ¿Qué combinación caracteriza mejor un "Lakehouse"?**

* **A. Object storage barato + capa de tablas ACID + metadatos/catálogo + múltiples motores**
* B. Solo un DWH propietario sin acceso externo
* C. Solo data lake sin esquema, sin gobernanza
* D. OLTP con índices tradicionales y transacciones por fila

> **Respuesta correcta:** A

---

**15) ¿Cuál afirmación es más consistente sobre Iceberg/Delta vs. un motor propietario tipo Snowflake?**

* A. Iceberg y Delta son motores OLTP para transacciones por fila
* **B. Iceberg/Delta usan metadatos/log/manifiestos para ACID y skipping; motores propietarios gestionan metadatos de manera interna en su ecosistema**
* C. Delta no soporta ACID e Iceberg sí
* D. Snowflake no usa metadatos para optimizar lecturas

> **Respuesta correcta:** B

---

**16) ¿Qué describe mejor el rol de Analytics Engineering?**

* A. Reemplaza Data Engineering y elimina ingestión/EL
* **B. Se enfoca en modelado, tests, documentación, versionado y CI/CD de transformaciones (la "T" del ELT)**
* C. Solo diseña dashboards; no trabaja con datos transformados
* D. Solo hace machine learning y feature engineering

> **Respuesta correcta:** B

---

**17) En dbt, ¿qué diferencia es más precisa entre tests genéricos y singulares?**

* **A. Genéricos aplican a columnas relaciones comunes, singulares son reglas SQL custom**
* B. Genéricos solo validan tablas, singulares solo validan columnas
* C. Singulares no pueden fallar el pipeline
* D. Genéricos no se pueden ejecutar en CI

> **Respuesta correcta:** A

---

**18) (Seleccionar las verdaderas) Source freshness en dbt se relaciona con:**

* **A. Un campo `loaded_at_field` para medir retraso/latencia de datos**
* **B. Umbrales warn / error para SLA de actualización**
* C. Sustituir tests de integridad referencial
* **D. Detectar fuentes "stale" aunque el pipeline haya corrido**

> **Respuestas correctas:** A, B, D

---

**19) ¿Qué describe mejor un snapshot en dbt?**

* A. Backup físico de la base de datos completo
* **B. Captura histórico de cambios tipo SCD2 sobre filas/columnas rastreadas**
* C. Reemplaza la necesidad de dimensiones de fecha
* D. Solo sirve para logs de auditoría de ejecución

> **Respuesta correcta:** B

---

**20) (Seleccionar las verdaderas) Sobre "Star schema vs OBT (One Big Table)", ¿cuáles criterios son válidos?**

* **A. OBT puede simplificar consumo evitando joins "al vuelo"**
* **B. Star schema suele mejorar mantenibilidad/semántica y dimensiones conformadas**
* **C. El "mejor" depende de motor, patrón de consultas y costos de joins/duplicación**
* D. OBT siempre es superior porque elimina necesidad de modelado

> **Respuestas correctas:** A, B, C

---

**21) ¿Qué secuencia describe mejor Job -> Stage -> Task en Spark?**

* A. Job es unidad mínima; task agrupa stages
* **B. Job se dispara por una acción; stages se separan por límites de shuffle; tasks corren por partición**
* C. Stage se dispara por acción; job por partición
* D. Task solo existe en streaming

> **Respuesta correcta:** B

---

**22) ¿Qué diferencia práctica explica mejor por qué DataFrames suelen ser más rápidos que RDDs en datos estructurados?**

* A. RDD siempre es más rápido por estar más cerca de JVM
* **B. DataFrame permite optimización (Catalyst) y ejecución más eficiente en consulta/plan**
* C. RDD tiene schema y DataFrame no
* D. No hay diferencia; solo cambian nombres de funciones

> **Respuesta correcta:** B

---

**23) (Seleccionar las verdaderas) ¿Qué operaciones son más propensas a causar shuffle grande?**

* **A. `groupBy().agg(...)`**
* **B. `orderBy()` global**
* C. `select()` de columnas
* **D. join grande sin broadcast**

> **Respuestas correctas:** A, B, D

---

**24) ¿Qué estrategia de join típicamente evita shuffle cuando una tabla es suficientemente pequeña?**

* A. Sort-merge join
* **B. Broadcast join**
* C. Shuffle hash join
* D. Cross join

> **Respuesta correcta:** B

---

**25) ¿Cuál es la afirmación más correcta sobre `repartition(n)` vs. `coalesce(n)`?**

* A. `coalesce` siempre aumenta particiones y produce shuffle completo
* **B. `repartition` redistribuye (shuffle) para cambiar particiones; `coalesce` normalmente reduce particiones con menor movimiento**
* C. Ambos siempre hacen shuffle igual
* D. `repartition` solo cambia metadata sin mover datos

> **Respuesta correcta:** B

### Parte Práctica

#### Contexto Del Problema

**Megaline** es una empresa de telecomunicaciones que ofrece planes mensuales con una combinación de minutos, mensajes y datos móviles. La Gerencia quiere responder: **¿qué plan es más rentable y por qué?**

La empresa tiene 25 millones de clientes en todo USA, aproximadamente 10 TB de datos.

### Tablas fuente disponibles

* `megaline_users` — catálogo de usuarios, su plan contratado y fechas de creación/deserción
* `megaline_plans` — catálogo de planes con cuota mensual, límites incluidos y tarifas por excedente
* `megaline_calls` — eventos de llamadas (uso). Cada fila es una llamada
* `megaline_messages` — eventos de SMS. Cada fila es un mensaje
* `megaline_internet` — sesiones de internet. Cada fila es una sesión con MB consumidos

---

**1) Escribir el `docker-compose.yaml` para levantar la infraestructura que ustedes implementarían para la empresa.**

Se detallan los servicios para PostgreSQL, MageAI y para PySpark con Jupyter.

> **Ir a** [`docker-compose.yaml`](Práctico/docker-compose.yaml)

**2) Creen un `data-loader` genérico para traer los datos de las BDD con reintentos y chunking.**

Se utiliza el formato de Data Loader de MageAI para cargar los datos desde la base de datos original.

> **Ir a** [`data_loader.py`](Práctico/data_loader.py)

**3) Creen el diagrama ERD de modelamiento dimensional que implementan para la capa GOLD.**

Se detalla la tabla de hechos de `Usage` para cada evento de uso, y las dimensiones de `User`, `Plan` y `Date`.

> **Ir a** [`ERD.png`](Práctico/ERD.png)

**4) Estás creando la tabla de hechos con DBT de tu diagrama ERD, escribe solo el from y join con su clave de unión para crearla.**

Asumiendo la existencia de las tablas de la capa silver, se hacen los joins a las tablas de la capa original para crear la tabla de `Fct_Usage`.

> **Ir a** [`dbt_facts.sql`](Práctico/dbt_facts.sql)

**5) Al ser 10 TB de datos, necesitan usar Spark para resolver las preguntas de negocio. Usando PySpark creen el código para calcular el ingreso promedio de cada plan en 2025.**

Tomando las variables de entorno como conocidas y las dependencias configuradas, se cargan las tablas usando PySpark, se hacen los joins y se busca los resultados.

> **Ir a** [`pyspark.py`](Práctico/pyspark.py)

**Extra) Escribe el código SQL para crear la tabla de hechos, y el código para particionar. Escribir el particionamiento solo de Enero-Febrero 2025.**

Se detalla el particionamiento de la tabla de hechos, junto con las tablas particionadas para los meses de Enero y Febrero 2025.

> **Ir a** [`sql_facts_partition.sql`](Práctico/sql_facts_partition.sql)
