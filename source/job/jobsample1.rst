作业示例（基本）
======================

根据集群的不同队列、不同应用软件，示例 slurm 作业脚本。

作业提交流程
------------

1. 编写作业脚本

::

     vi test.slurm  # 根据需求，选择计算资源：CPU 或 GPU、所需核数、是否需要大内存

2. 提交作业

::

     sbatch test.slurm

3. 查看作业和资源

::

     squeue       # 查看正在排队或运行的作业

或

::

     sacct        # 查看过去 24 小时内已完成的作业

集群资源实时状态查询

::

     sinfo        # 若有 idle 或 mix 状态的节点，排队会比较快


各队列作业示例
--------------

small
~~~~~~~~~~

small 队列 slurm 脚本示例

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=small      # small 队列
   #SBATCH -n 20                 # 总核数需 <=20
   #SBATCH --ntasks-per-node=20   # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err


cpu
~~~~~~~~

cpu 队列 slurm 脚本示例：多节点（160 核）


.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=cpu        # cpu 队列
   #SBATCH -n 160                # 总核数 160 
   #SBATCH --ntasks-per-node=40   # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err


cpu 队列 slurm 脚本示例：单节点（40 核）

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=cpu        # cpu 队列
   #SBATCH -n 40                 # 总核数 40 
   #SBATCH --ntasks-per-node=40   # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err 


cpu 队列 slurm 脚本示例：单节点（20核），比如为了独占整个节点的大内存

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=cpu        # cpu 队列
   #SBATCH -n 20                 # 总核数 20 
   #SBATCH --ntasks-per-node=20   # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err 
   #SBATCH --exclusive            # 独占节点（核数小于 40，cpu 队列必须加上此命令）


huge
~~~~~~~~~

huge 队列 slurm 脚本示例：单节点（20 核，最高可用 80 核）

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test         # 作业名 
   #SBATCH --partition=huge        # huge 队列
   #SBATCH -n 20 # 总核数 20 
   #SBATCH --ntasks-per-node=20    # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

192c6t
~~~~~~

192c6t 队列 slurm 脚本示例：单节点（96 核，最高可用 192 核）

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=192c6      # 192c6t 队列
   #SBATCH -n 96                 # 总核数 96 
   #SBATCH --ntasks-per-node=96   # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

dgx2
~~~~

dgx2 队列 slurm 脚本示例：单节点，分配 2 块 GPU，GPU:CPU 配比 1:6

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test        # 作业名 
   #SBATCH --partition=dgx2       # dgx2 队列
   #SBATCH -N 1                    
   #SBATCH --ntasks-per-node=1
   #SBATCH --cpus-per-task=12     # 1:6 的 GPU:CPU 配比  
   #SBATCH --gres=gpu:2           # 2 块 GPU 
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

arm128c256g
~~~~~~~~~~~

arm128c256g 队列 slurm 脚本示例：单节点60核

.. code:: bash

    #!/bin/bash

    #SBATCH --job-name=test
    #SBATCH --partition=arm128c256g
    #SBATCH -N 1
    #SBATCH --ntasks-per-node=60
    #SBATCH --output=%j.out
    #SBATCH --error=%j.err

    source /lustre/share/singularity/commercial-app/vasp/activate arm

    mpirun -n $SLURM_NTASKS vasp_std

常用软件作业示例
----------------

下面根据不同应用软件，示例 slurm 作业脚本

LAMMPS 作业示例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cpu 队列 slurm 脚本示例 LAMMPS

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test         # 作业名 
   #SBATCH --partition=cpu         # cpu 队列
   #SBATCH -n 80                  # 总核数 80 
   #SBATCH --ntasks-per-node=40    # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

   module load lammps

   srun --mpi=pmi2 lmp -i YOUR_INPUT_FILE


GROMACS 作业示例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cpu 队列 slurm 脚本示例 GROMACS

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test         # 作业名 
   #SBATCH --partition=cpu         # cpu 队列
   #SBATCH -n 80                  # 总核数 80 
   #SBATCH --ntasks-per-node=40    # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

   module load gromacs/2020-cpu

   srun --mpi=pmi2 gmx_mpi mdrun -deffnm -s test.tpr -ntomp 1

Quantum ESPRESSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cpu 队列 slurm 脚本示例 Quantum ESPRESSO

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test         # 作业名 
   #SBATCH --partition=cpu         # cpu 队列
   #SBATCH -n 80                  # 总核数 80 
   #SBATCH --ntasks-per-node=40    # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

   module load quantum-espresso

   srun --mpi=pmi2 pw.x -i test.in



OpenFOAM
~~~~~~~~~~~~~~~~~~~~~~

cpu 队列 slurm 脚本示例 OpenFoam

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test         # 作业名 
   #SBATCH --partition=cpu         # cpu 队列
   #SBATCH -n 80                  # 总核数 80 
   #SBATCH --ntasks-per-node=40    # 每节点核数
   #SBATCH --output=%j.out 
   #SBATCH --error=%j.err

   module load openfoam

   srun --mpi=pmi2 icoFoam -parallel

TensorFlow
~~~~~~~~~~~~~~~~~~~~~~~~

gpu 队列 slurm 脚本示例 TensorFlow

.. code:: bash

   #!/bin/bash

   #SBATCH -J test 
   #SBATCH -p dgx2 
   #SBATCH -o %j.out 
   #SBATCH -e %j.err
   #SBATCH -N 1 
   #SBATCH --ntasks-per-node=1 
   #SBATCH --cpus-per-task=12
   #SBATCH --gres=gpu:2

   module load miniconda3 
   source activate tf-env

   python -c ’import tensorflow as tf; \
          print(tf.__version__); \
          print(tf.test.is_gpu_available());’ 


其它示例
--------


Job Array 阵列作业
~~~~~~~~~~~~~~~~~~

一批作业，若所需资源和内容相似，可借助 Job Array 批量提交。Job Array
中的每一个作业在调度时视为独立的作业。

cpu 队列 slurm 脚本示例 array

.. code:: bash

   #!/bin/bash
   
   #SBATCH --job-name=test           # 作业名
   #SBATCH --partition=small         # small 队列
   #SBATCH -n 1                      # 总核数 1
   #SBATCH --ntasks-per-node=1       # 每节点核数
   #SBATCH --output=array_%A_%a.out
   #SBATCH --error=array_%A_%a.err
   #SBATCH --array=1-20%10           # 总共 20 个子任务，每次最多同时运行 10 个

   echo $SLURM_ARRAY_TASK_ID


作业状态邮件提醒
~~~~~~~~~~~~~~~~

--mail-type= 指定状态发生时，发送邮件通知: ALL, BEGIN, END, FAIL

small 队列 slurm 脚本示例：邮件提醒

.. code:: bash

   #!/bin/bash

   #SBATCH --job-name=test           
   #SBATCH --partition=small         
   #SBATCH -n 20                     
   #SBATCH --ntasks-per-node=20
   #SBATCH --output=%j.out
   #SBATCH --error=%j.err
   #SBATCH --mail-type=end           # 作业结束时，邮件提醒
   #SBATCH --mail-user=XX@sjtu.edu.cn

