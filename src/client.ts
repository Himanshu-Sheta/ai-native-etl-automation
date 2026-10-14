import { PipelineExecutionResult, ETLValidationRule, DataRecord } from './types';

export class AIEtlClient {
  private baseUrl: string;

  constructor(baseUrl: string = 'http://localhost:8000') {
    this.baseUrl = baseUrl;
  }

  async triggerPipeline(
    datasetName: string,
    records: DataRecord[],
    rules: ETLValidationRule[]
  ): Promise<PipelineExecutionResult> {
    const payload = {
      dataset_name: datasetName,
      raw_records: records,
      validation_rules: rules
    };

    const response = await fetch(`${this.baseUrl}/api/v1/etl/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`ETL Pipeline trigger failed with status ${response.status}`);
    }

    return (await response.json()) as PipelineExecutionResult;
  }

  async getHealthStatus(): Promise<{ status: string; uptime_seconds: number }> {
    const res = await fetch(`${this.baseUrl}/health`);
    return await res.json();
  }
}
