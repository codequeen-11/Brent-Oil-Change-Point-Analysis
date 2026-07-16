import { useEffect, useState } from "react";
import api from "../api/api";

export default function useDashboard() {

    const [prices, setPrices] = useState([]);

    const [events, setEvents] = useState([]);

    const [summary, setSummary] = useState(null);

    const [changePoint, setChangePoint] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function fetchData() {

            try {

                const [
                    pricesRes,
                    eventsRes,
                    summaryRes,
                    cpRes,
                ] = await Promise.all([

                    api.get("/prices"),

                    api.get("/events"),

                    api.get("/summary"),

                    api.get("/change-point"),

                ]);

                setPrices(pricesRes.data);

                setEvents(eventsRes.data);

                setSummary(summaryRes.data);

                setChangePoint(cpRes.data);

            } catch (err) {

                console.error(err);

            } finally {

                setLoading(false);

            }

        }

        fetchData();

    }, []);

    return {

        prices,

        events,

        summary,

        changePoint,

        loading,

    };
}