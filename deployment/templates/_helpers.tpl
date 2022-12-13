{{/*
Expand the name of the chart.
*/}}
{{- define "vjcms.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "vjcms.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "vjcms.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "vjcms.image" -}}
"{{ .Values.image.registry }}{{ .Values.image.repository }}:{{ .Values.image.tag }}"
{{- end }}

{{/*
Common labels
*/}}
{{- define "vjcms.labels" -}}
helm.sh/chart: {{ include "vjcms.chart" . }}
{{ include "vjcms.selectorLabels" . }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "vjcms.selectorLabels" -}}
app.kubernetes.io/name: {{ include "vjcms.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}