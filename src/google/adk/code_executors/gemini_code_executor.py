# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.genai import types
from pydantic import Field
from typing_extensions import override

from ..agents.invocation_context import InvocationContext
from ..models import LlmRequest
from .base_code_executor import BaseCodeExecutor
from .code_execution_utils import CodeExecutionInput
from .code_execution_utils import CodeExecutionResult


class GeminiCodeExecutor(BaseCodeExecutor):
  """A code executor for Gemini 2.0+ models to exeute code."""

  @override
  def execute_code(
      self,
      invocation_context: InvocationContext,
      code_execution_input: CodeExecutionInput,
  ) -> CodeExecutionResult:
    pass

  def process_llm_request(self, llm_request: LlmRequest) -> None:
    """Pre-process the LLM request for Gemini 2.0+ models to use the code execution tool."""
    if llm_request.model and llm_request.model.startswith("gemini-2"):
      llm_request.config = llm_request.config or types.GenerateContentConfig()
      llm_request.config.tools = llm_request.config.tools or []
      llm_request.config.tools.append(
          types.Tool(code_execution=types.ToolCodeExecution())
      )
      return
    raise ValueError(
        "Gemini code execution tool is not supported for model"
        f" {llm_request.model}"
    )
