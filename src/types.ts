/**
 * Core type definitions for AI-Native ETL pipeline execution and validation.
 */

export type JobStatus = 'PENDING' | 'EXTRACTING' | 'TRANSFORMING' | 'VALIDATING' | 'COMPLETED' | 'FAILED';

export interface DataRecord {
  id: string | number;
  [key: string]: any;
}

export interface ETLValidationRule {
  field: string;
  ruleType: 'NON_NULL' | 'TYPE_CHECK' | 'RANGE_CHECK' | 'REGEX' | 'SEMANTIC_AI_CHECK';
  parameters?: Record<string, any>;
  severity: 'WARNING' | 'CRITICAL';
}

export interface ValidationIssue {
  rowId: string | number;
  field: string;
  ruleViolated: string;
  errorMessage: string;
  suggestedFix?: string;
}

export interface PipelineExecutionResult {
  jobId: string;
  status: JobStatus;
  rowsExtracted: number;
  rowsLoaded: number;
  anomaliesDetected: number;
  issues: ValidationIssue[];
  aiReasoningSummary: string;
  durationMs: number;
}
