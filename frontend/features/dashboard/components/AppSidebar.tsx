"use client";

import {
  FileText,
  History,
  Home,
  Settings,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

const items = [
  {
    label: "Dashboard",
    icon: Home,
  },
  {
    label: "History",
    icon: History,
  },
  {
    label: "Reports",
    icon: FileText,
  },
];


export function AppSidebar() {
  return (
    <aside className="flex h-full w-20 flex-col items-center border-r py-6">
      <div className="flex flex-1 flex-col items-center gap-4">
        {items.map(({ label, icon: Icon }) => (
          <Button
            key={label}
            variant={label === "Dashboard" ? "default" : "ghost"}
            size="icon"
            aria-label={label}
          >
            <Icon className="size-5" />
          </Button>
        ))}
      </div>

      <Separator className="mb-4 w-10" />

      <Button
        variant="ghost"
        size="icon"
        aria-label="Settings"
      >
        <Settings className="size-5" />
      </Button>
    </aside>
  );
}