import createClient from "openapi-fetch";
import type { paths } from "./schema";

export function createApiClient(baseUrl: string, getToken: () => string | null) {
  const client = createClient<paths>({ baseUrl });
  client.use({
    onRequest({ request }) {
      const token = getToken();
      if (token) request.headers.set("Authorization", `Visitor ${token}`);
      return request;
    },
  });
  return client;
}
