"use client";

import { motion } from "motion/react";
import type { LucideIcon } from "lucide-react";

import { Card } from "@/components/ui/card";
import { StatusIndicator } from "./StatusIndicator";

type Props = {
  title: string;
  description: string;
  icon: LucideIcon;
  status: "pending" | "running" | "completed" | "failed";
  color: "blue" | "purple" | "orange" | "emerald";
};

const iconColors = {
  blue: "bg-blue-100 text-blue-600",
  purple: "bg-violet-100 text-violet-600",
  orange: "bg-orange-100 text-orange-600",
  emerald: "bg-emerald-100 text-emerald-600",
};

export function WorkflowCard({
  title,
  description,
  icon: Icon,
  status,
  color,
}: Props) {
  return (
    <motion.div whileHover={{ y: -2 }} transition={{ duration: 0.2 }}>
      <Card className="glass-card rounded-2xl p-4">
        <div className="flex items-start justify-between">
          {/* Left */}
          <div className="flex items-center gap-4">
            <div
              className={`flex h-12 w-12 items-center justify-center rounded-xl ${iconColors[color]}`}
            >
              <Icon className="h-6 w-6" />
            </div>

            <div>
              <h3 className="text-base font-semibold">{title}</h3>

              <p className="mt-1 text-sm text-muted-foreground">
                {description}
              </p>
            </div>
          </div>

          {/* Right */}
          
          <div className="flex items-center gap-2">
          <StatusIndicator status={status} />

          {status === "completed" && (
            <span className="text-xs text-emerald-600">
              Done
            </span>
          )}

          {status === "running" && (
            <span className="text-xs text-blue-600">
              Running
            </span>
          )}

          {status === "pending" && (
            <span className="text-xs text-muted-foreground">
              Pending
            </span>
          )}

          {status === "failed" && (
            <span className="text-xs text-red-600">
              Failed
            </span>
          )}
        </div>
        
        </div>
      </Card>
    </motion.div>
  );
}