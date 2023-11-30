*******************
提交MPI作业
*******************


1. 命令行提交MPI作业
======================
MPI（Message Passing Interface）是一种并行计算的标准，用于在多个进程之间进行通信和协调。以下是命令行通过 Slurm 运行 MPI 程序的基本步骤：

- 加载集群上的 MPI模块： 首先，确保在你的系统上安装了 MPI。常见的 MPI 实现包括 Open MPI 和 MPICH。你可以使用module load 加载MPI模块：

.. code:: bash

  # 加载openmpi
  module load openmpi4/4.1.5

  # 加载mpich
  module load mpich/3.4.3-ucx


- 编写 MPI 程序： 编写一个使用 MPI 接口的并行程序。MPI 程序通常使用 C、C++ 或 Fortran 编写。以下是一个简单的 MPI 程序的示例，使用 C 语言编写：

.. code:: c

  // mpi_hello.c
  #include <mpi.h>
  #include <stdio.h>

  int main(int argc, char** argv) {
      MPI_Init(&argc, &argv);

      int rank, size;
      MPI_Comm_rank(MPI_COMM_WORLD, &rank);
      MPI_Comm_size(MPI_COMM_WORLD, &size);

      printf("Hello from process %d of %d\n", rank, size);

      MPI_Finalize();
      return 0;
  }


- 编译 MPI 程序： 使用 MPI 编译器(openmpi、mpich)来编译你的程序。MPI 编译器通常带有特定的前缀，比如 mpicc。

.. code:: bash

  # 使用openmpi编译

  module purge
  module load gnu/12.2.0
  module load openmpi4/4.1.5
  mpicc mpi_hello.c -o mpi_hello

.. code:: bash

  # 使用mpich编译
  module purge
  module load gnu/12.2.0
  module load mpich/3.4.3-ucx
  mpicc mpi_hello.c -o mpi_hello

通过slurm脚本运行 MPI 程序： 使用slurm脚本分配计算资源,运行 MPI 可执行程序。

- 编写slurm的作业脚本文件:mpi_hello.slurm

.. code:: bash

  #!/bin/bash
  #SBATCH --job-name='MPI_11291644'
  #SBATCH --chdir=/home/my_test_dir
  #SBATCH --partition=compute
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=4
  #SBATCH --time=0-24:00

  module purge
  module load gnu/12.2.0
  module load openmpi4/4.1.5
  mpirun  ./mpi_hello

其中，#SBATCH 行是 Slurm 的作业配置选项，用于指定作业的参数。解释如下::

  --job-name='MPI_11291644'：指定作业的名称。
  --chdir=/home/my_test_dir：指定作业运行的工作目录。
  --partition=compute：指定作业运行在哪个分区（compute 分区）。
  --nodes=1：指定使用的节点数。
  --ntasks-per-node=2：指定每个节点上运行的任务数。
  --time=0-24:00：指定作业的最大运行时间为 24 小时。

- 提交作业到SLURM集群运行

.. code:: bash

  sbatch mpi_hello.slurm

上述命令将在 4 个进程上运行 mpi_hello 程序。你可以根据需要调整 `--ntasks-per-node` 的值来更改MPI进程数。



2. LiCO客户端提交MPI程序作业
=============================

- 打开作业模板>HPC>MPI：打开LiCO作业模板,点击进入MPI作业模板。

- 填写模板参数:
   
  **运行环境**：MPI作业运行使用的运行环境，默认使用openMPI运行环境。

  **MPI程序**：为编译的MPI可执行程序，请将编译时使用的MPI运行环境与运行时选用的MPI运行环境保持一致。

.. image:: ./mpi_job.png
  :width: 900px

- 查看运行结果: 可以通过LiCO作业页面查看作业运行过程中的日志信息。

.. image:: ./mpi_job_run.png
  :width: 900px

