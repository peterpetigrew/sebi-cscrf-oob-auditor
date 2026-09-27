\# Out-of-Band SEBI CSCRF Compliance Auditor



A lightweight, asynchronous compliance monitor engineered specifically for High-Frequency Trading (HFT) environments.



\## The Architectural Challenge

The SEBI CSCRF mandate requires strict API access monitoring and a 6-hour incident reporting window. However, implementing inline security checks introduces unacceptable latency bottlenecks into microsecond trading pipelines.



\## The Solution

This auditor operates entirely \*\*Out-of-Band (OOB)\*\*. By ingesting JSONL log streams via network taps or port mirroring, it flags unauthorized API probes and calculates SEBI regulatory deadlines asynchronously.



\*\*Result:\*\* 100% regulatory compliance monitoring with \*\*0.00ms latency impact\*\* on the core C++/FPGA order execution path.



\## Usage

```bash

python sebi\_auditor.py --stream trading\_logs.jsonl

