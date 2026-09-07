import { SiteExperience } from "@/components/site-experience";
import { resolveView } from "@/lib/content";

export default async function Home({ searchParams }: { searchParams: Promise<{ vista?: string | string[] }> }) {
  const params = await searchParams;
  return <SiteExperience activeView={resolveView(params.vista)} />;
}
