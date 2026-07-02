import { api } from "@/lib/api";
import type {
  GenerateRequest,
  GenerateResponse,
} from "@/types/report";

class ReportService {
  async generate(
    payload: GenerateRequest
  ): Promise<GenerateResponse> {
    const { data } = await api.post<GenerateResponse>(
      "/generate",
      payload
    );

    return data;
  }
}

export const reportService = new ReportService();